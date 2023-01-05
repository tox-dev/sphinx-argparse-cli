from __future__ import annotations

import os
import re
import sys
from argparse import (
    SUPPRESS,
    Action,
    ArgumentParser,
    HelpFormatter,
    _ArgumentGroup,
    _StoreFalseAction,
    _StoreTrueAction,
    _SubParsersAction,
)
from collections import defaultdict, namedtuple
from typing import Any, Iterator, cast

from docutils.nodes import (
    Element,
    Node,
    Text,
    bullet_list,
    fully_normalize_name,
    list_item,
    literal,
    literal_block,
    paragraph,
    reference,
    section,
    strong,
    title,
    whitespace_normalize_name,
)
from docutils.parsers.rst.directives import flag, positive_int, unchanged, unchanged_required
from docutils.parsers.rst.states import RSTState, RSTStateMachine
from docutils.statemachine import StringList
from sphinx.domains.std import StandardDomain
from sphinx.locale import __
from sphinx.util.docutils import SphinxDirective
from sphinx.util.logging import getLogger

TextAsDefault = namedtuple("TextAsDefault", ["text"])


def make_id(key: str) -> str:
    return "-".join(key.split()).rstrip("-")


logger = getLogger(__name__)


class SphinxArgparseCli(SphinxDirective):
    name = "sphinx_argparse_cli"
    has_content = False
    option_spec = {
        "module": unchanged_required,
        "func": unchanged_required,
        "hook": flag,
        "prog": unchanged,
        "title": unchanged,
        "description": unchanged,
        "usage_width": positive_int,
        "group_title_prefix": unchanged,
        "group_sub_title_prefix": unchanged,
        "no_default_values": unchanged,
    }

    def __init__(
        self,
        name: str,
        arguments: list[str],
        options: dict[str, str | None],
        content: StringList,
        lineno: int,
        content_offset: int,
        block_text: str,
        state: RSTState,
        state_machine: RSTStateMachine,
    ):
        options.setdefault("group_title_prefix", None)
        options.setdefault("group_sub_title_prefix", None)
        super().__init__(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)
        self._parser: ArgumentParser | None = None
        self._std_domain: StandardDomain = cast(StandardDomain, self.env.get_domain("std"))

    @property
    def parser(self) -> ArgumentParser:
        if self._parser is None:
            module_name, attr_name = self.options["module"], self.options["func"]
            parser_creator = getattr(__import__(module_name, fromlist=[attr_name]), attr_name)
            if "hook" in self.options:
                original_parse_known_args = ArgumentParser.parse_known_args
                ArgumentParser.parse_known_args = _argparse_parse_known_args_hook  # type: ignore
                try:
                    parser_creator()
                except HookError as hooked:
                    self._parser = hooked.parser
                finally:
                    ArgumentParser.parse_known_args = original_parse_known_args  # type: ignore
            else:
                self._parser = parser_creator()

            del sys.modules[module_name]  # no longer needed cleanup
            if self._parser is None:
                raise self.error("Failed to hook argparse to get ArgumentParser")

            if "prog" in self.options:
                self._parser.prog = self.options["prog"]
        return self._parser

    def load_sub_parsers(self) -> Iterator[tuple[list[str], str, ArgumentParser]]:
        top_sub_parser = self.parser._subparsers
        if not top_sub_parser:
            return
        parser_to_args: dict[int, list[str]] = defaultdict(list)
        str_to_parser: dict[str, ArgumentParser] = {}
        sub_parser: _SubParsersAction[ArgumentParser] = top_sub_parser._group_actions[0]  # type: ignore
        for key, parser in sub_parser._name_parser_map.items():
            parser_to_args[id(parser)].append(key)
            str_to_parser[key] = parser
        done_parser: set[int] = set()
        for name, parser in sub_parser.choices.items():
            parser_id = id(parser)
            if parser_id in done_parser:
                continue
            done_parser.add(parser_id)
            aliases = parser_to_args[id(parser)]
            aliases.remove(name)
            # help is stored in a pseudo action
            help_msg = next((a.help for a in sub_parser._choices_actions if a.dest == name), None) or ""
            yield aliases, help_msg, parser

    def run(self) -> list[Node]:
        # construct headers
        self.env.note_reread()  # this document needs to be always updated
        title_text = self.options.get("title", f"{self.parser.prog} - CLI interface").strip()
        if title_text.strip() == "":
            home_section: Element = paragraph()
        else:
            home_section = section("", title("", Text(title_text)), ids=[make_id(title_text)], names=[title_text])

        description = self.options.get("description", self.parser.description)
        if description:
            desc_paragraph = paragraph("", Text(description))
            home_section += desc_paragraph
        # construct groups excluding sub-parsers
        home_section += self._mk_usage(self.parser)
        for group in self.parser._action_groups:
            if not group._group_actions or group is self.parser._subparsers:
                continue
            home_section += self._mk_option_group(group, prefix=self.parser.prog.split("/")[-1])
        # construct sub-parser
        for aliases, help_msg, parser in self.load_sub_parsers():
            home_section += self._mk_sub_command(aliases, help_msg, parser)
        return [home_section]

    def _mk_option_group(self, group: _ArgumentGroup, prefix: str) -> section:
        sub_title_prefix: str = self.options["group_sub_title_prefix"]
        title_prefix = self.options["group_title_prefix"]

        title_text = self._build_opt_grp_title(group, prefix, sub_title_prefix, title_prefix)
        title_ref: str = f"{prefix}{' ' if prefix else ''}{group.title}"
        ref_id = make_id(title_ref)
        # the text sadly needs to be prefixed, because otherwise the autosectionlabel will conflict
        header = title("", Text(title_text))
        group_section = section("", header, ids=[ref_id], names=[ref_id])
        if group.description:
            group_section += paragraph("", Text(group.description))
        self._register_ref(ref_id, title_text, group_section)
        opt_group = bullet_list()
        for action in group._group_actions:
            point = self._mk_option_line(action, prefix)
            opt_group += point
        group_section += opt_group
        return group_section

    def _build_opt_grp_title(self, group: _ArgumentGroup, prefix: str, sub_title_prefix: str, title_prefix: str) -> str:
        title_text, elements = "", prefix.split(" ")
        if title_prefix is not None:
            title_prefix = title_prefix.replace("{prog}", elements[0])
            if title_prefix:
                title_text += f"{title_prefix} "
            if " " in prefix:
                if sub_title_prefix is not None:
                    title_text = self._append_title(title_text, sub_title_prefix, elements[0], " ".join(elements[1:]))
                else:
                    title_text += f"{' '.join(prefix.split(' ')[1:])} "
        else:
            if " " in prefix:
                if sub_title_prefix is not None:
                    title_text += f"{elements[0]} "
                    title_text = self._append_title(title_text, sub_title_prefix, elements[0], " ".join(elements[1:]))
                else:
                    title_text += f"{' '.join(elements[:2])} "
            else:
                title_text += f"{prefix} "
        title_text += group.title or ""
        return title_text

    def _mk_option_line(self, action: Action, prefix: str) -> list_item:
        line = paragraph()
        as_key = action.dest
        if action.metavar:
            as_key = action.metavar if isinstance(action.metavar, str) else action.metavar[0]
        if action.option_strings:
            first = True
            is_flag = action.nargs == 0
            for opt in action.option_strings:
                if first:
                    first = False
                else:
                    line += Text(", ")
                self._mk_option_name(line, prefix, opt)
                if not is_flag:
                    line += Text(" ")
                    line += literal(text=as_key.upper())
        else:
            self._mk_option_name(line, prefix, as_key)

        point = list_item("", line, ids=[])
        if action.help:
            help_text = load_help_text(action.help)
            temp = paragraph()
            self.state.nested_parse(StringList(help_text.split("\n")), 0, temp)
            line += Text(" - ")
            for content in cast(paragraph, temp.children[0]).children:
                line += content
        if (
            "no_default_values" not in self.options
            and action.default != SUPPRESS
            and not re.match(r".*[ (]default[s]? .*", (action.help or ""))
            and not isinstance(action, (_StoreTrueAction, _StoreFalseAction))
        ):
            line += Text(" (default: ")
            line += literal(text=str(action.default).replace(os.getcwd(), "{cwd}"))
            line += Text(")")
        return point

    def _mk_option_name(self, line: paragraph, prefix: str, opt: str) -> None:
        ref_id = make_id(f"{prefix}-{opt}")
        ref_title = f"{prefix} {opt}"
        ref = reference("", refid=ref_id, reftitle=ref_title)
        line.attributes["ids"].append(ref_id)
        st = strong()
        st += literal(text=opt)
        ref += st
        self._register_ref(ref_id, ref_title, ref, is_cli_option=True)
        line += ref

    def _register_ref(self, ref_name: str, ref_title: str, node: Element, is_cli_option: bool = False) -> None:
        doc_name = self.env.docname
        normalize_name = whitespace_normalize_name if is_cli_option else fully_normalize_name
        if self.env.config.sphinx_argparse_cli_prefix_document:
            name = normalize_name(f"{doc_name}:{ref_name}")
        else:
            name = normalize_name(ref_name)
        if name in self._std_domain.labels:
            logger.warning(
                __("duplicate label %s, other instance in %s"),
                name,
                self.env.doc2path(self._std_domain.labels[name][0]),
                location=node,
                type="sphinx-argparse-cli",
                subtype=self.env.docname,
            )
        self._std_domain.anonlabels[name] = doc_name, ref_name
        self._std_domain.labels[name] = doc_name, ref_name, ref_title

    def _mk_sub_command(self, aliases: list[str], help_msg: str, parser: ArgumentParser) -> section:
        sub_title_prefix: str = self.options["group_sub_title_prefix"]
        title_prefix: str = self.options["group_title_prefix"]

        title_text = self._build_sub_cmd_title(parser, sub_title_prefix, title_prefix)
        title_ref: str = parser.prog
        if aliases:
            aliases_text: str = f" ({', '.join(aliases)})"
            title_text += aliases_text
            title_ref += aliases_text
        title_text = title_text.strip()
        ref_id = make_id(title_ref)
        group_section = section("", title("", Text(title_text)), ids=[ref_id], names=[title_ref])
        self._register_ref(ref_id, title_ref, group_section)

        command_desc = (parser.description or help_msg or "").strip()
        if command_desc:
            desc_paragraph = paragraph("", Text(command_desc))
            group_section += desc_paragraph
        group_section += self._mk_usage(parser)
        for group in parser._action_groups:
            if not group._group_actions:  # do not show empty groups
                continue
            group_section += self._mk_option_group(group, prefix=parser.prog)
        return group_section

    def _build_sub_cmd_title(self, parser: ArgumentParser, sub_title_prefix: str, title_prefix: str) -> str:
        title_text, elements = "", parser.prog.split(" ")
        if title_prefix is not None:
            title_prefix = title_prefix.replace("{prog}", elements[0])
            if title_prefix:
                title_text += f"{title_prefix} "
            if sub_title_prefix is not None:
                title_text = self._append_title(title_text, sub_title_prefix, elements[0], elements[1])
            else:
                title_text += elements[1]
        else:
            if sub_title_prefix is not None:
                title_text += f"{elements[0]} "
                title_text = self._append_title(title_text, sub_title_prefix, elements[0], elements[1])
            else:
                title_text += parser.prog
        return title_text.rstrip()

    @staticmethod
    def _append_title(title_text: str, sub_title_prefix: str, prog: str, sub_cmd: str) -> str:
        if sub_title_prefix:
            sub_title_prefix = sub_title_prefix.replace("{prog}", prog)
            sub_title_prefix = sub_title_prefix.replace("{subcommand}", sub_cmd)
            title_text += f"{sub_title_prefix} "
        return title_text

    def _mk_usage(self, parser: ArgumentParser) -> literal_block:
        parser.formatter_class = lambda prog: HelpFormatter(prog, width=self.options.get("usage_width", 100))
        texts = parser.format_usage()[len("usage: ") :].splitlines()
        texts = [line if at == 0 else f"{' ' * (len(parser.prog) + 1)}{line.lstrip()}" for at, line in enumerate(texts)]
        return literal_block("", Text("\n".join(texts)))


SINGLE_QUOTE = re.compile(r"[']+(.+?)[']+")
DOUBLE_QUOTE = re.compile(r'["]+(.+?)["]+')
CURLY_BRACES = re.compile(r"[{](.+?)[}]")


def load_help_text(help_text: str) -> str:
    single_quote = SINGLE_QUOTE.sub("``'\\1'``", help_text)
    double_quote = DOUBLE_QUOTE.sub('``"\\1"``', single_quote)
    literal_curly_braces = CURLY_BRACES.sub("``{\\1}``", double_quote)
    return literal_curly_braces


class HookError(Exception):
    def __init__(self, parser: ArgumentParser):
        self.parser = parser


def _argparse_parse_known_args_hook(self: ArgumentParser, *args: Any, **kwargs: Any) -> None:  # noqa: U100
    raise HookError(self)


__all__ = ("SphinxArgparseCli",)
