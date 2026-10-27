# Changelog

All notable changes to this project will be documented in this file.

<!-- towncrier release notes start -->

<a name="release-1-24-1"></a>

## 1.24.1 (2026-10-27)

<a name="release-1-24-1-fixed"></a>

### Fixed

- Fix repository links in the PyPI project description ([#376](https://github.com/tox-dev/sphinx-argparse-cli/pull/376))
  by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-24-0"></a>

## 1.24.0 (2026-10-10)

<a name="release-1-24-0-added"></a>

### Added

- Require Python 3.11 and use Python 3.15 by default ([#369](https://github.com/tox-dev/sphinx-argparse-cli/pull/369))
  by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-23-0"></a>

## 1.23.0 (2026-08-27)

<a name="release-1-23-0-added"></a>

### Added

- Register CLI arguments as Sphinx program options so `:option:` can link to them
  ([#346](https://github.com/tox-dev/sphinx-argparse-cli/pull/346)) by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-23-0-fixed"></a>

### Fixed

- Render positional arguments declared before `add_subparsers()`
  ([#347](https://github.com/tox-dev/sphinx-argparse-cli/pull/347)) by [@gaborbernat](https://github.com/gaborbernat).
- Keep apostrophes in help text ([#349](https://github.com/tox-dev/sphinx-argparse-cli/pull/349)) by
  [@gaborbernat](https://github.com/gaborbernat).
- Render argument groups without a title ([#350](https://github.com/tox-dev/sphinx-argparse-cli/pull/350)) by
  [@gaborbernat](https://github.com/gaborbernat).
- Make `:hook:` intercept `parse_intermixed_args()` ([#351](https://github.com/tox-dev/sphinx-argparse-cli/pull/351)) by
  [@gaborbernat](https://github.com/gaborbernat).
- Preserve raw formatter line breaks and render subcommand epilogs
  ([#352](https://github.com/tox-dev/sphinx-argparse-cli/pull/352)) by [@gaborbernat](https://github.com/gaborbernat).
- Render option metavars, argument counts, and choices as in usage
  ([#353](https://github.com/tox-dev/sphinx-argparse-cli/pull/353)) by [@gaborbernat](https://github.com/gaborbernat).
- Render list and multi-paragraph help under the option
  ([#354](https://github.com/tox-dev/sphinx-argparse-cli/pull/354)) by [@gaborbernat](https://github.com/gaborbernat).
- Expand argparse format specifiers in help text ([#355](https://github.com/tox-dev/sphinx-argparse-cli/pull/355)) by
  [@gaborbernat](https://github.com/gaborbernat).
- Strip ANSI colors from usage blocks ([#356](https://github.com/tox-dev/sphinx-argparse-cli/pull/356)) by
  [@gaborbernat](https://github.com/gaborbernat).
- Skip subcommands whose help is suppressed ([#357](https://github.com/tox-dev/sphinx-argparse-cli/pull/357)) by
  [@gaborbernat](https://github.com/gaborbernat).
- Expand `{subcommand}` to the subcommand name chain ([#358](https://github.com/tox-dev/sphinx-argparse-cli/pull/358))
  by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-23-0-documentation"></a>

### Documentation

- Name `force_refs_lower` correctly in the changelog ([#348](https://github.com/tox-dev/sphinx-argparse-cli/pull/348))
  by [@gaborbernat](https://github.com/gaborbernat).
- Explain that help text uses reStructuredText ([#359](https://github.com/tox-dev/sphinx-argparse-cli/pull/359)) by
  [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-22-1"></a>

## 1.22.1 (2026-08-11)

<a name="release-1-22-0"></a>

## 1.22.0 (2026-07-20)

<a name="release-1-22-0-added"></a>

### Added

- Add Python 3.15 support ([#331](https://github.com/tox-dev/sphinx-argparse-cli/pull/331)) by
  [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-21-4"></a>

## 1.21.4 (2026-07-06)

<a name="release-1-21-4-fixed"></a>

### Fixed

- Keep Sphinx smart quotes from rewriting `--option` names in descriptions, epilogs, and help text
  ([#322](https://github.com/tox-dev/sphinx-argparse-cli/pull/322)) by [@mmulqueen](https://github.com/mmulqueen).

<a name="release-1-21-3"></a>

## 1.21.3 (2026-03-19)

<a name="release-1-21-3-fixed"></a>

### Fixed

- Handle formatter subclasses and wrap preformatted blocks
  ([#297](https://github.com/tox-dev/sphinx-argparse-cli/pull/297)) by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-21-2"></a>

## 1.21.2 (2026-03-16)

<a name="release-1-21-2-fixed"></a>

### Fixed

- Avoid a crash when a toctree title is empty ([#296](https://github.com/tox-dev/sphinx-argparse-cli/pull/296)) by
  [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-21-1"></a>

## 1.21.1 (2026-03-02)

<a name="release-1-21-1-documentation"></a>

### Documentation

- Restructure the README around common use cases ([#292](https://github.com/tox-dev/sphinx-argparse-cli/pull/292)) by
  [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-21-0"></a>

## 1.21.0 (2026-03-02)

<a name="release-1-21-0-fixed"></a>

### Fixed

- Render all tuple metavar elements and suppress `None` defaults
  ([#287](https://github.com/tox-dev/sphinx-argparse-cli/pull/287)) by [@gaborbernat](https://github.com/gaborbernat).
- Propagate a `:prog:` override to subcommands ([#288](https://github.com/tox-dev/sphinx-argparse-cli/pull/288)) by
  [@gaborbernat](https://github.com/gaborbernat).
- Handle multi-word program names in group titles ([#289](https://github.com/tox-dev/sphinx-argparse-cli/pull/289)) by
  [@gaborbernat](https://github.com/gaborbernat).
- Remove a missing custom CSS reference ([#290](https://github.com/tox-dev/sphinx-argparse-cli/pull/290)) by
  [@gaborbernat](https://github.com/gaborbernat).
- Use a section node when a toctree title is empty ([#291](https://github.com/tox-dev/sphinx-argparse-cli/pull/291)) by
  [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-20-1"></a>

## 1.20.1 (2025-10-08)

<a name="release-1-20-1-fixed"></a>

### Fixed

- Disable color codes while parsing a CLI ([#252](https://github.com/tox-dev/sphinx-argparse-cli/pull/252)) by
  [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-20-0"></a>

## 1.20.0 (2025-10-08)

<a name="release-1-20-0-added"></a>

### Added

- Add Python 3.14 support and end support for Python 3.10
  ([#251](https://github.com/tox-dev/sphinx-argparse-cli/pull/251)) by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-19-0"></a>

## 1.19.0 (2024-12-10)

<a name="release-1-19-0-added"></a>

### Added

- Handle nested subparsers ([#207](https://github.com/tox-dev/sphinx-argparse-cli/pull/207)) by
  [@ianw](https://github.com/ianw).

<a name="release-1-18-2"></a>

## 1.18.2 (2024-09-18)

<a name="release-1-18-1"></a>

## 1.18.1 (2024-09-08)

<a name="release-1-18-1-documentation"></a>

### Documentation

- Fix the README by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-18-0"></a>

## 1.18.0 (2024-09-08)

<a name="release-1-18-0-added"></a>

### Added

- Add Python 3.13 support and end support for Python 3.9
  ([#184](https://github.com/tox-dev/sphinx-argparse-cli/pull/184)) by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-17-0"></a>

## 1.17.0 (2024-08-06)

<a name="release-1-17-0-added"></a>

### Added

- Add `force_refs_lower` for `:ref:` links with mixed-case program names and arguments
  ([#179](https://github.com/tox-dev/sphinx-argparse-cli/pull/179)) by [@ianw](https://github.com/ianw).

<a name="release-1-16-0"></a>

## 1.16.0 (2024-06-18)

<a name="release-1-16-0-added"></a>

### Added

- Declare the extension safe for parallel reads by Sphinx
  ([#171](https://github.com/tox-dev/sphinx-argparse-cli/pull/171)) by [@JSCU-CNI](https://github.com/JSCU-CNI).

<a name="release-1-15-0"></a>

## 1.15.0 (2024-04-17)

<a name="release-1-15-0-added"></a>

### Added

- Support Sphinx 7.3 and end support for Python 3.8 ([#163](https://github.com/tox-dev/sphinx-argparse-cli/pull/163)) by
  [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-14-0"></a>

## 1.14.0 (2024-03-22)

<a name="release-1-14-0-added"></a>

### Added

- Allow content inside the directive ([#158](https://github.com/tox-dev/sphinx-argparse-cli/pull/158)) by
  [@mondeja](https://github.com/mondeja).

<a name="release-1-13-1"></a>

## 1.13.1

<a name="release-1-13-1-fixed"></a>

### Fixed

- Fix multiline handling of group descriptions ([#152](https://github.com/tox-dev/sphinx-argparse-cli/pull/152)) by
  [@mayrholu](https://github.com/mayrholu).

<a name="release-1-13-0"></a>

## 1.13.0

<a name="release-1-13-0-added"></a>

### Added

- Add option to show usage before description ([#148](https://github.com/tox-dev/sphinx-argparse-cli/pull/148)) by
  [@mayrholu](https://github.com/mayrholu).

<a name="release-1-13-0-fixed"></a>

### Fixed

- Don't render arguments with `help=argparse.SUPPRESS` ([#149](https://github.com/tox-dev/sphinx-argparse-cli/pull/149))
  by [@mayrholu](https://github.com/mayrholu).
- Show epilogue if present in the command description ([#146](https://github.com/tox-dev/sphinx-argparse-cli/pull/146))
  by [@mayrholu](https://github.com/mayrholu).

<a name="release-1-12-0"></a>

## 1.12.0

<a name="release-1-12-0-added"></a>

### Added

- Support rendering with `argparse.RawDescriptionHelpFormatter`
  ([#144](https://github.com/tox-dev/sphinx-argparse-cli/pull/144)) by [@mayrholu](https://github.com/mayrholu).

<a name="release-1-11-1"></a>

## 1.11.1

<a name="release-1-11-1-added"></a>

### Added

- Declare Python 3.12 support ([#102](https://github.com/tox-dev/sphinx-argparse-cli/pull/102)) by
  [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-11-1-fixed"></a>

### Fixed

- Fix broken end-user references ([#95](https://github.com/tox-dev/sphinx-argparse-cli/pull/95)) by
  [@webknjaz](https://github.com/webknjaz).

<a name="release-1-11-0"></a>

## 1.11.0

<a name="release-1-11-0-added"></a>

### Added

- End support for Sphinx 6.1 by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-10-0"></a>

## 1.10.0

<a name="release-1-10-0-added"></a>

### Added

- Add the option to override the generated `default` part of the CLI parameter description
  ([#56](https://github.com/tox-dev/sphinx-argparse-cli/pull/56)) by [@berhoel](https://github.com/berhoel).

<a name="release-1-9-0"></a>

## 1.9.0

<a name="release-1-9-0-added"></a>

### Added

- Add the option to override the description using the `description` attribute of the directive
  ([#45](https://github.com/tox-dev/sphinx-argparse-cli/pull/45)) by [@Schamper](https://github.com/Schamper).
- Add the option to retrieve the arguments by hooking argparse, in cases where `func` consumes the arguments and does
  not return them ([#46](https://github.com/tox-dev/sphinx-argparse-cli/pull/46)) by
  [@Schamper](https://github.com/Schamper).

<a name="release-1-8-3"></a>

## 1.8.3

<a name="release-1-8-3-fixed"></a>

### Fixed

- Fix project links after the move to tox-dev by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-8-2"></a>

## 1.8.2

<a name="release-1-8-2-fixed"></a>

### Fixed

- Don't raise label clashing warnings for options which only differ between upper and lower case
  ([#34](https://github.com/tox-dev/sphinx-argparse-cli/pull/34)) by [@mondeja](https://github.com/mondeja).

<a name="release-1-8-1"></a>

## 1.8.1

<a name="release-1-8-1-fixed"></a>

### Fixed

- Fix reference clashing for options which only differ between upper and lower case
  ([#32](https://github.com/tox-dev/sphinx-argparse-cli/pull/32)) by [@mondeja](https://github.com/mondeja).
- Do not render default values for `store_true` and `store_false` actions
  ([#30](https://github.com/tox-dev/sphinx-argparse-cli/pull/30)) by [@mondeja](https://github.com/mondeja).

<a name="release-1-8-0"></a>

## 1.8.0

<a name="release-1-8-0-added"></a>

### Added

- Support Python 3.10 ([#13](https://github.com/tox-dev/sphinx-argparse-cli/pull/13)) by
  [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-7-0"></a>

## 1.7.0

<a name="release-1-7-0-added"></a>

### Added

- Support for adding custom subsection group title prefix (`group_title_prefix` and `group_sub_title_prefix` directive
  arguments) ([#12](https://github.com/tox-dev/sphinx-argparse-cli/pull/12)) by [@mondeja](https://github.com/mondeja).

<a name="release-1-6-0"></a>

## 1.6.0 (2021-04-15)

<a name="release-1-6-0-added"></a>

### Added

- Support for using the `ref` sphinx role to refer to all anchor-able objects generated by the tool by
  [@gaborbernat](https://github.com/gaborbernat).
- Flags now have their reference title set (for the HTML builder this is shown when hover over the reference) by
  [@gaborbernat](https://github.com/gaborbernat).
- Added a sphinx flag `sphinx_argparse_cli_prefix_document` (by default `False`) to avoid reference clashes when
  multiple documents generate the same reference labels by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-6-0-fixed"></a>

### Fixed

- Anchors generated no longer collapse multiple subsequent `-` characters (to avoid clash when there's a flag and a
  positional argument with the same name) by [@gaborbernat](https://github.com/gaborbernat).
- The root `prog` name now is prefixed for the root level optional/positional arguments' header (to avoid multiple
  anchors with the same id when multiple commands are documented in the same document) by
  [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-5-2"></a>

## 1.5.2

<a name="release-1-5-2-changes"></a>

### Changes

- Prefer a parser's description over its help message for subcommands by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-5-1"></a>

## 1.5.1 (2021-04-15)

<a name="release-1-5-1-documentation"></a>

### Documentation

- Update the README by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-5-0"></a>

## 1.5.0 (2021-02-13)

<a name="release-1-5-0-changes"></a>

### Changes

- Display the metavar (fallback to dest) if the action has more than one argument (this is inline with how usage is
  displayed) by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-4-0"></a>

## 1.4.0 (2021-02-13)

<a name="release-1-4-0-changes"></a>

### Changes

- Command line arguments are now bold to highlight them even further from the help text by
  [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-3-0"></a>

## 1.3.0 (2021-02-13)

<a name="release-1-3-0-added"></a>

### Added

- Add support for changing the usage width via the `usage_width` option on the directive by
  [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-3-0-changes"></a>

### Changes

- Help messages are now interpreted as reStructuredText by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-3-0-fixed"></a>

### Fixed

- Mark document as always needs update (as the underlying content is coming from outside the sphinx documents) by
  [@gaborbernat](https://github.com/gaborbernat).
- Matching curly braces, single and double quotes in help text will be marked as string literals by
  [@gaborbernat](https://github.com/gaborbernat).
- Help messages containing the `default(s)` word do not show the default value (as often this indicates the default is
  already documented in the help text) by [@gaborbernat](https://github.com/gaborbernat).

<a name="release-1-2-0"></a>

## 1.2.0 (2021-02-05)

<a name="release-1-2-0-added"></a>

### Added

- Add support for changing (removing) the title via the `title` attribute of the directive
  ([#3](https://github.com/tox-dev/sphinx-argparse-cli/pull/3)) by [@mondeja](https://github.com/mondeja).

<a name="release-1-1-0"></a>

## 1.1.0 (2021-02-05)

<a name="release-1-1-0-added"></a>

### Added

- Add support for setting the parser's `prog` with the directive's `prog` attribute
  ([#1](https://github.com/tox-dev/sphinx-argparse-cli/pull/1)) by [@mondeja](https://github.com/mondeja).

<a name="release-1-0-0"></a>

## 1.0.0 (2021-02-05)

<a name="release-1-0-0-added"></a>

### Added

- First version by [@gaborbernat](https://github.com/gaborbernat).
