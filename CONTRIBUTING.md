# Contributing

Run the tests and type checker with `tox -e 3.15,type`. Run `prek run --all-files` before pushing a pull request.

## Release notes

Add a `changelog.d/+short-name.<type>.md` fragment when a pull request changes what package users can use or observe.
Use one fragment per user-facing change. The release workflow links each fragment to its merged squash pull request.

| Type          | Changelog section | Use for                                                    |
| ------------- | ----------------- | ---------------------------------------------------------- |
| `feature`     | Added             | New capabilities and Python support additions or removals  |
| `change`      | Changes           | Changed behavior that remains available                    |
| `bugfix`      | Fixed             | Corrected behavior                                         |
| `doc`         | Documentation     | Documentation changes users need to know about             |
| `breaking`    | Breaking changes  | Changes that require users to update code or configuration |
| `security`    | Security          | Security fixes users need to act on                        |
| `performance` | Performance       | User-visible speed or resource improvements                |
| `deprecation` | Deprecated        | Supported behavior scheduled for removal                   |
| `removal`     | Removed           | Removed user-facing capabilities other than Python support |
| `packaging`   | Packaging         | Install, wheel, or distribution changes                    |

Use `skip news` for a pull request with no user-facing change. The label can be applied after the pull request opens. A
fragment still has to be valid when the label is present. Dependabot, pre-commit.ci, and repository automation receive
the label when their pull request has no fragment.

The release workflow credits the pull request author. If several people authored the change, add their linked GitHub
handles in one `by` phrase in the fragment. Omit bots and reviewers.
