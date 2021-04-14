# Changelog

All notable changes to this project will be documented in this file.

## 1.5.1 (2021-04-15)

- For sub-commands use the parser description first as description and only then fallback to the help message

## 1.5.0 (2021-02-13)

- Display the metavar (fallback to dest) if the action has more than one argument (this is inline with how usage is
  displayed).

## 1.4.0 (2021-02-13)

- Command line arguments are now bold to highlight them even further from the help text

## 1.3.0 (2021-02-13)

- Add support for changing the usage width via the `usage_width` option on the directive
- Mark document as always needs update (as the underlying content is coming from outside the sphinx documents)
- Help messages is now interpreted as reStructuredText
- Matching curly braces, single and double quotes in help text will be marked as string literals
- Help messages containing the `default(s)` word do not show the default value (as often this indicates the default is
  already documented in the help text)

## 1.2.0 (2021-02-05)

- Add support for changing (removing) the title via the `title` attribute of the directive.

## 1.1.0 (2021-02-05)

- Add support for setting the `prog` of the parser via the a `prog` attribute of the directive.

## 1.0.0 (2021-02-05)

- First version.
