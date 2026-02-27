This directory stores Towncrier news fragments.

Naming format:
- `<ticket>.added.md`
- `<ticket>.changed.md`
- `<ticket>.fixed.md`

If you do not have a ticket number, use `+` as the ticket value.

Examples:
- `123.added.md`
- `+.fixed.md`

Release workflow:
1. Add one or more fragment files in this directory.
2. Run `towncrier build --version <new-version>`.
3. Commit updated `CHANGELOG.md` and remove consumed fragments.
