# sphinx-argparse-cli

[![PyPI](https://img.shields.io/pypi/v/sphinx-argparse-cli?style=flat-square)](https://pypi.org/project/sphinx-argparse-cli)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/sphinx-argparse-cli?style=flat-square)](https://pypi.org/project/sphinx-argparse-cli)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sphinx-argparse-cli?style=flat-square)](https://pypi.org/project/sphinx-argparse-cli)
[![Downloads](https://static.pepy.tech/badge/sphinx-argparse-cli/month)](https://pepy.tech/project/sphinx-argparse-cli)
[![PyPI - License](https://img.shields.io/pypi/l/sphinx-argparse-cli?style=flat-square)](https://opensource.org/licenses/MIT)
[![check](https://github.com/tox-dev/sphinx-argparse-cli/actions/workflows/check.yaml/badge.svg)](https://github.com/tox-dev/sphinx-argparse-cli/actions/workflows/check.yaml)

Render CLI arguments (sub-commands friendly) defined by the argparse module.

## Getting started

Install the package:

```bash
python -m pip install sphinx-argparse-cli
```

Add the extension to your `conf.py`:

```python
extensions = ["sphinx_argparse_cli"]
```

Use the directive in any reStructuredText file:

```rst
.. sphinx_argparse_cli::
  :module: my_project.cli
  :func: build_parser
```

`:module:` points to the Python module containing the parser, and `:func:` names a zero-argument function that returns
an `ArgumentParser`. Build your docs and the full CLI reference appears automatically.

## How-to guides

### Override the program name

By default the program name comes from the parser. Use `:prog:` to replace it:

```rst
.. sphinx_argparse_cli::
  :module: my_project.cli
  :func: build_parser
  :prog: my-cli
```

### Hook into a parser that is not returned

When a function creates and uses a parser internally without returning it, set the `:hook:` flag to intercept
`argparse.ArgumentParser`:

```rst
.. sphinx_argparse_cli::
  :module: my_project.cli
  :func: main
  :hook:
  :prog: my-cli
```

### Customize section titles

Control how group and subcommand headings are rendered with `:group_title_prefix:` and `:group_sub_title_prefix:`. Both
accept `{prog}` and the sub-title also accepts `{subcommand}`:

```rst
.. sphinx_argparse_cli::
  :module: my_project.cli
  :func: build_parser
  :group_title_prefix: {prog}
  :group_sub_title_prefix: {prog} {subcommand}
```

### Suppress default values

Hide `(default: ...)` annotations from the output:

```rst
.. sphinx_argparse_cli::
  :module: my_project.cli
  :func: build_parser
  :no_default_values:
```

### Control usage display

Set the character width for usage lines and optionally show usage before the description:

```rst
.. sphinx_argparse_cli::
  :module: my_project.cli
  :func: build_parser
  :usage_width: 80
  :usage_first:
```

### Override title, description, or epilog

Replace auto-detected values, or pass an empty string to suppress them entirely:

```rst
.. sphinx_argparse_cli::
  :module: my_project.cli
  :func: build_parser
  :title: Custom Title
  :description: Custom description text.
  :epilog:
```

### Cross-reference generated anchors

The directive registers Sphinx reference labels for every command, group, and flag. Use the `:ref:` role to link to
them.

With `sphinx_argparse_cli_prefix_document = False` (default):

```rst
:ref:`tox-optional-arguments`
:ref:`tox-run`
:ref:`tox-run---magic`
```

With `sphinx_argparse_cli_prefix_document = True` (anchors prefixed by document name, avoids clashes across documents):

```rst
:ref:`cli:tox-optional-arguments`
:ref:`cli:tox-run`
:ref:`cli:tox-run---magic`
```

The anchor text is visible after the `#` in the URL when you click a heading.

### Handle mixed-case references

Sphinx `:ref:` only supports lower-case targets. When your program name or flags contain capital letters, set
`:force_refs_lower:` to convert them — each upper-case letter becomes its lower-case form prefixed with `_` (e.g. `A`
becomes `_a`):

```rst
.. sphinx_argparse_cli::
  :module: my_project.cli
  :func: build_parser
  :force_refs_lower:
```

For a program named `SampleProgram`:

```rst
:ref:`_sample_program--a`   .. flag -a
:ref:`_sample_program--_a`  .. flag -A
```

If you do not need Sphinx `:ref:` cross-references you can leave this off to keep mixed-case anchors in the HTML output,
but enabling it later will change existing anchor URLs.

### Add extra content after generated docs

Any content nested inside the directive is appended after the generated CLI documentation:

```rst
.. sphinx_argparse_cli::
  :module: my_project.cli
  :func: build_parser

  Extra notes or examples rendered after the CLI reference.
```

## Reference

### Directive options

| Option                     | Type   | Default                  | Description                                                                    |
| -------------------------- | ------ | ------------------------ | ------------------------------------------------------------------------------ |
| `:module:`                 | string | **required**             | Python module path where the parser is defined                                 |
| `:func:`                   | string | **required**             | Zero-argument function that returns an `ArgumentParser`                        |
| `:prog:`                   | string | parser's `prog`          | Override the displayed program name                                            |
| `:hook:`                   | flag   | off                      | Intercept `ArgumentParser` instead of expecting `func` to return it            |
| `:title:`                  | string | `<prog> - CLI interface` | Custom title; empty string suppresses it                                       |
| `:description:`            | string | parser's description     | Custom description; empty string suppresses it                                 |
| `:epilog:`                 | string | parser's epilog          | Custom epilog; empty string suppresses it                                      |
| `:usage_width:`            | int    | `100`                    | Character width for usage lines                                                |
| `:usage_first:`            | flag   | off                      | Show usage before the description                                              |
| `:group_title_prefix:`     | string | `{prog}`                 | Heading prefix for groups; `{prog}` is replaced with the program name          |
| `:group_sub_title_prefix:` | string | `{prog} {subcommand}`    | Heading prefix for subcommand groups; supports `{prog}` and `{subcommand}`     |
| `:no_default_values:`      | flag   | off                      | Suppress `(default: ...)` annotations                                          |
| `:force_refs_lower:`       | flag   | off                      | Lower-case reference anchors with `_` prefix for capitals (for `:ref:` compat) |

### Configuration values (`conf.py`)

| Name                                  | Type | Default | Description                                                      |
| ------------------------------------- | ---- | ------- | ---------------------------------------------------------------- |
| `sphinx_argparse_cli_prefix_document` | bool | `False` | Prefix reference anchors with the document name to avoid clashes |

## Live examples

- [tox](https://tox.wiki/en/latest/cli_interface.html)
- [pypa-build](https://pypa-build.readthedocs.io/en/latest/#python-m-build)
- [mdpo](https://mondeja.github.io/mdpo/latest/cli.html)
