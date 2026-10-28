# Security policy

sphinx-argparse-cli is a Sphinx extension that renders the command-line interface an `argparse` parser defines. This
policy says how to report a security problem and how we decide whether a report is one.

## Reporting a vulnerability

**Do not open a public issue for a security problem.** Use
[GitHub's private vulnerability reporting](https://github.com/tox-dev/sphinx-argparse-cli/security/advisories/new). If
you do not have a GitHub account, or you are a Tidelift subscriber, report through the
[Tidelift security contact](https://tidelift.com/security) instead; Tidelift coordinates the fix and the disclosure with
us. If neither works for you, email [gaborjbernat@gmail.com](mailto:gaborjbernat@gmail.com).

Include what the attacker controls and what they gain, the steps or a proof of concept, and the versions and platform
you tested. Write the report yourself; unreviewed tool or model output takes longer to triage.

## What to expect

Volunteers maintain sphinx-argparse-cli, with no on-call rotation. We aim to acknowledge a report within **5 working
days** and assess it within **15 working days**. Fixes are developed in a private fork attached to the draft advisory,
ship in a new release, and the advisory, with a CVE requested through GitHub, goes out with that release. The default
embargo is **90 days** from the report; we agree any change with the reporter. We credit reporters in the advisory under
the name they choose, or not at all. There is no bug bounty.

## Supported versions

Only the latest release receives fixes. Confirm the problem reproduces on it before reporting.

## Vulnerability or bug

A report is a vulnerability when an attacker who controls only an input that the [threat model](THREAT_MODEL.md) lists
as untrusted breaks a guarantee sphinx-argparse-cli makes. A report that first needs control of something the threat
model trusts, such as the documented project's code or the Sphinx configuration, is a bug: we fix it in the open and
publish no advisory. Classify by who supplies the dangerous input, not by how bad the outcome sounds.

**In scope**

- The directive importing a module, or calling a function, other than the ones its `:module:` and `:func:` options name.
- The extension reading or writing files beyond the Sphinx build's own outputs.

**Out of scope**

- Code that runs when the directive imports the module and calls the parser factory: that is the documented project's
  code, trusted like every module autodoc imports.
- Markup in help strings: the extension parses them as reStructuredText on purpose, so they are trusted like the code
  that defines them.
- Markup the documentation author writes around the directive.
- Sphinx and docutils behavior.

If you cannot tell which side a finding falls on, report it privately and we will decide.
