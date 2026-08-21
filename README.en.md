<div align="center">
    <a href="https://pypi.python.org/pypi/ChatTree">
        <img src="https://img.shields.io/pypi/v/ChatTree.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatTree/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatTree/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
    <a href="https://arch.gh.wzhecnu.cn/ChatTree/">
        <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
    </a>
</div>

<div align="center">

English | [简体中文](README.md)
</div>

# ChatTree

`ChatTree` is the ChatArch Python CLI package shell for tree-oriented workflows. The public CLI currently exposes truthful root-level package information entries only. Future tree capabilities must update Python APIs, the CLI tree, docs, and tests together.

## Quick Start

```bash
pip install ChatTree
chattree --help
chattree --version
chattree --tree
chattree --tree-brief
```

Development environment:

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```

## CLI Tree

ChatTree uses the shared `chatstyle.add_tree_option()` integration to generate full and brief trees from the registered Click command surface. The current CLI is root-only, so both views contain the same nodes.

```text
chattree
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`chattree hello` is not public CLI; it is a scaffold example leftover and must fail.

## CLI Contract

- The root command is explicitly named `chattree` and exposes `--version`, `--tree`, and `--tree-brief`.
- `chatstyle>=0.2.0,<0.3.0` renders both trees from the registered Click surface; the package does not maintain a local renderer.
- The package currently has no env/profile/config behavior, so it does not depend on ChatEnv. Future configuration must register a typed provider and use `chatenv>=0.2.10,<0.3.0` with ChatEnv-managed storage paths.
- The current root-only entrypoint only prints package and command metadata. It does not read or mutate project trees or handle sensitive values.

## Documentation

- Documentation home: https://arch.gh.wzhecnu.cn/ChatTree/
- CLI tree: https://arch.gh.wzhecnu.cn/ChatTree/cli-tree/
- English docs: https://arch.gh.wzhecnu.cn/ChatTree/en/

## Development Notes

Read `DEVELOP.md` and `AGENTS.md` before expanding commands, and keep `--tree`, `--tree-brief`, README, MkDocs, tests, and changelog synchronized.
