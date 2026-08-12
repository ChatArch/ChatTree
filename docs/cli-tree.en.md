# CLI Tree

`chattree --tree` is generated from the real registered Click command surface. `ChatTree` currently exposes root-level package information entries only and no business subcommands; a template `hello` command is not part of the public interface.

## Top-level command

```text
chattree  # ChatTree placeholder package for tree-oriented workflows
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## Status Contract

- `chattree --help` must expose `--tree`.
- `chattree --tree` must exit 0 and list only real registered commands/options.
- `chattree hello` must fail; `hello` is not a business command.
- Future tree capabilities must add reusable Python APIs first, then CLI commands, and then update this page.
