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
    _SubParsersAction,
)
from collections import defaultdict, namedtuple
from typing import Iterator, Set, cast

from docutils.nodes import (
    Element,
    Node,
    Text,
    bullet_list,
    list_item,
    literal,
    literal_block,
    paragraph,
    reference,
    section,
    title,
)
from docutils.parsers.rst.directives import unchanged, unchanged_required
from docutils.parsers.rst.states import RSTState, RSTStateMachine
from docutils.statemachine import StringList
from sphinx.util.docutils import SphinxDirective

TextAsDefault = namedtuple("TextAsDefault", ["text"])


def make_id(key: str) -> str:
    return re.sub(r"-{2,}", "-", re.sub(r"\W", "-", key)).rstrip("-").lower()


class SphinxArgparseCli(SphinxDirective):
    name = "sphinx_argparse_cli"
    has_content = False
    option_spec = {
        "module": unchanged_required,
        "func": unchanged_required,
        "prog": unchanged,
        "title": unchanged,
    }

    def __init__(
        self,
        name: str,
        arguments: list[str],
        options: dict[str, str],
        content: StringList,
        lineno: int,
        content_offset: int,
        block_text: str,
        state: RSTState,
        state_machine: RSTStateMachine,
    ):
        super().__init__(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)
        self._parser: ArgumentParser | None = None

    @property
    def parser(self) -> ArgumentParser:
        if self._parser is None:
            module_name, attr_name = self.options["module"], self.options["func"]
            parser_creator = getattr(__import__(module_name, fromlist=[attr_name]), attr_name)
            self._parser = parser_creator()
            if "prog" in self.options:
                self._parser.prog = self.options["prog"]
            del sys.modules[module_name]  # no longer needed cleanup
        return self._parser

    def load_sub_parsers(self) -> Iterator[tuple[list[str], str, ArgumentParser]]:
        top_sub_parser = self.parser._subparsers  # noqa
        if not top_sub_parser:
            return
        parser_to_args: dict[int, list[str]] = defaultdict(list)
        str_to_parser: dict[str, ArgumentParser] = {}
        sub_parser = cast(_SubParsersAction, top_sub_parser._group_actions[0])  # noqa
        for key, parser in sub_parser._name_parser_map.items():  # noqa
            parser_to_args[id(parser)].append(key)
            str_to_parser[key] = parser
        done_parser: set[int] = set()
        for name, parser in sub_parser.choices.items():  # noqa
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
        title_text = self.options.get("title", f"{self.parser.prog} - CLI interface").strip()
        if title_text.strip() == "":
            home_section: Element = paragraph()
        else:
            home_section = section("", title("", Text(title_text)), ids=[make_id(title_text)], names=[title_text])

        if self.parser.description:
            desc_paragraph = paragraph("", Text(self.parser.description))
            home_section += desc_paragraph
        # construct groups excluding sub-parsers
        home_section += self._mk_usage(self.parser)
        for group in self.parser._action_groups:  # noqa
            if not group._group_actions or group is self.parser._subparsers:  # noqa
                continue
            home_section += self._mk_option_group(group, prefix="")
        # construct sub-parser
        for aliases, help_msg, parser in self.load_sub_parsers():
            home_section += self._mk_sub_command(aliases, help_msg, parser)
        return [home_section]

    def _mk_option_group(self, group: _ArgumentGroup, prefix: str) -> section:
        title_text = f"{prefix}{' ' if prefix else ''}{group.title}"
        ref_id = make_id(title_text)
        # the text sadly needs to be prefixed, because otherwise the autosectionlabel will conflict
        header = title("", Text(title_text))
        group_section = section("", header, ids=[ref_id], names=[ref_id])
        if group.description:
            group_section += paragraph("", Text(group.description))
        opt_group = bullet_list()
        for action in group._group_actions:  # noqa
            point = self._mk_option_line(action, prefix)
            opt_group += point
        group_section += opt_group
        return group_section

    def _mk_option_line(self, action: Action, prefix: str) -> list_item:  # noqa
        line = paragraph()
        if action.option_strings:
            first = True
            for opt in action.option_strings:
                if first:
                    first = False
                else:
                    line += Text(", ")
                ref_id = make_id(f"{prefix}-{opt}")
                ref = reference("", refid=ref_id)
                line.attributes["ids"].append(ref_id)
                ref += literal(text=opt)
                line += ref
        else:
            as_key = (
                action.dest
                if action.metavar is None
                else (action.metavar if isinstance(action.metavar, str) else action.metavar[0])
            )
            ref_id = make_id(f"{prefix}-{as_key}")
            ref = reference("", refid=ref_id)
            line.attributes["ids"].append(ref_id)
            ref += literal(text=as_key)
            line += ref
        point = list_item("", line, ids=[])
        if action.help:
            line += Text(" - ")
            line += Text(action.help)
        if action.default != SUPPRESS:
            line += Text(" (default: ")
            line += literal(text=str(action.default).replace(os.getcwd(), "{cwd}"))
            line += Text(")")
        return point

    def _mk_sub_command(self, aliases: list[str], help_msg: str, parser: ArgumentParser) -> section:
        title_text = f"{parser.prog}"
        if aliases:
            title_text += f" ({', '.join(aliases)})"
        group_section = section("", title("", Text(title_text)), ids=[make_id(title_text)], names=[title_text])
        if help_msg:
            desc_paragraph = paragraph("", Text(help_msg))
            group_section += desc_paragraph
        group_section += self._mk_usage(parser)
        for group in parser._action_groups:  # noqa
            if not group._group_actions:  # do not show empty groups
                continue
            group_section += self._mk_option_group(group, prefix=parser.prog)
        return group_section

    def _mk_usage(self, parser: ArgumentParser) -> literal_block:
        parser.formatter_class = lambda prog: HelpFormatter(prog, width=100)
        texts = parser.format_usage()[len("usage: ") :].splitlines()
        texts = [line if at == 0 else f"{' ' * (len(parser.prog) + 1)}{line.lstrip()}" for at, line in enumerate(texts)]
        return literal_block("", Text("\n".join(texts)))


__all__ = ("SphinxArgparseCli",)
