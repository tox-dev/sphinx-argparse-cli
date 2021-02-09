# sphinx-argparse-cli

[![PyPI](https://img.shields.io/pypi/v/sphinx-argparse-cli?style=flat-square)](https://pypi.org/project/sphinx-argparse-cli)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/sphinx-argparse-cli?style=flat-square)](https://pypi.org/project/sphinx-argparse-cli)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sphinx-argparse-cli?style=flat-square)](https://pypi.org/project/sphinx-argparse-cli)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/sphinx-argparse-cli?style=flat-square)](https://pypistats.org/packages/sphinx-argparse-cli)
[![PyPI - License](https://img.shields.io/pypi/l/sphinx-argparse-cli?style=flat-square)](https://opensource.org/licenses/MIT)
![check](https://github.com/gaborbernat/sphinx-argparse-cli/workflows/check/badge.svg?branch=main)
[![codecov](https://codecov.io/gh/gaborbernat/sphinx-argparse-cli/branch/main/graph/badge.svg)](https://codecov.io/gh/pypa/virtualenv)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

Render CLI arguments (sub-commands friendly) defined by the argparse module. For live demo checkout the documentation of
[tox](https://tox.readthedocs.io/en/rewrite/cli_interface.html) and [mdpo](https://mdpo.readthedocs.io/en/latest/cli.html#command-line-interfaces).

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

- the module path to where the parser is defined,
- a no argument function within that module that once called returns the constructed
  [argparse](https://docs.python.org/3/library/argparse.html) parser
- (optional) a program name that overwrites the autodiscovered running argument parser
- (optional) a `:title:` argument which, when provided, overwrites the `<prog> - CLI interface` title added by default
  and when empty, will not be included

```rst
.. sphinx_argparse_cli::
  :module: a_project.cli
  :func: build_parser
  :prog: my-cli-program
```
