# sphinx-argparse-cli

[![PyPI](https://img.shields.io/pypi/v/sphinx-argparse-cli?style=flat-square)](https://pypi.org/project/sphinx-argparse-cli)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/sphinx-argparse-cli?style=flat-square)](https://pypi.org/project/sphinx-argparse-cli)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sphinx-argparse-cli?style=flat-square)](https://pypi.org/project/sphinx-argparse-cli)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/sphinx-argparse-cli?style=flat-square)](https://pypistats.org/packages/sphinx-argparse-cli)
[![PyPI - License](https://img.shields.io/pypi/l/sphinx-argparse-cli?style=flat-square)](https://opensource.org/licenses/MIT)
![check](https://github.com/tox-dev/sphinx-argparse-cli/workflows/check/badge.svg?branch=main)

Render CLI arguments (sub-commands friendly) defined by the argparse module. For live demo checkout the documentation of
[tox](https://tox.readthedocs.io/en/rewrite/cli_interface.html),
[python-build](https://pypa-build.readthedocs.io/en/latest/#python-m-build) and
[mdpo](https://mdpo.readthedocs.io/en/master/cli.html#command-line-interfaces).

## installation

```bash
python -m pip install sphinx-argparse-cli
```

## enable in your `conf.py`

```python
# just add it to your list of extensions to load within conf.py
extensions = ["sphinx_argparse_cli"]
```

## use

Within the reStructuredText files use the `sphinx_argparse_cli` directive that takes, at least, two arguments:

| Name                   | Description                                                                                                                                                                      |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| module                 | the module path to where the parser is defined                                                                                                                                   |
| func                   | the name of the function that once called with no arguments constructs the parser                                                                                                |
| prog                   | (optional) when provided, overwrites the `<prog>` name.                                                                                                                          |
| hook                   | (optional) hook `argparse` to retrieve the parser if `func` uses a parser instead of returning it.                                                                               |
| title                  | (optional) when provided, overwrites the `<prog> - CLI interface` title added by default and when empty, will not be included                                                    |
| description            | (optional) when provided, overwrites the description and when empty, will not be included                                                                                        |
| usage_width            | (optional) how large should usage examples be - defaults to 100 character                                                                                                        |
| group_title_prefix     | (optional) groups subsections title prefixes, accepts the string `{prog}` as a replacement for the program name - defaults to `{prog}`                                           |
| group_sub_title_prefix | (optional) subcommands groups subsections title prefixes, accepts replacement of `{prog}` and `{subcommand}` for program and subcommand name - defaults to `{prog} {subcommand}` |
| no_default_values      | (optional) supresses generation of `default` entries                                                                                                                             |

For example:

```rst
.. sphinx_argparse_cli::
  :module: a_project.cli
  :func: build_parser
  :prog: my-cli-program
```

If you have code that creates and uses a parser but does not return it, you can specify the `:hook:` flag:

```rst
.. sphinx_argparse_cli::
  :module: a_project.cli
  :func: main
  :hook:
  :prog: my-cli-program
```

### Refer to generated content

The tool will register reference links to all anchors. This means that you can use the sphinx `ref` role to refer to
both the (sub)command title/groups and every flag/argument. The tool offers a configuration flag
`sphinx_argparse_cli_prefix_document` (change by setting this variable in `conf.py` - by default `False`). This option
influences the reference ids generated. If it's false the reference will be the anchor id (the text appearing after the
`'#` in the URI once you click on it). If it's true the anchor id will be prefixed by the document name (this is useful
to avoid reference label clash when the same anchors are generated in multiple documents).

For example in case of a `tox` command, and `sphinx_argparse_cli_prefix_document=False` (default):

- to refer to the optional arguments group use `` :ref:`tox-optional-arguments`  ``,
- to refer to the run subcommand use `` :ref:`tox-run`  ``,
- to refer to flag `--magic` of the `run` sub-command use `` :ref:`tox-run---magic`  ``.

For example in case of a `tox` command, and `sphinx_argparse_cli_prefix_document=True`, and the current document name
being `cli`:

- to refer to the optional arguments group use `` :ref:`cli:tox-optional-arguments`  ``,
- to refer to the run subcommand use `` :ref:`cli:tox-run`  ``,
- to refer to flag `--magic` of the `run` sub-command use `` :ref:`cli:tox-run---magic`  ``.
