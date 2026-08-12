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
chattree --version
chattree --tree
```

Development environment:

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```

## CLI Tree

```text
chattree  # ChatTree placeholder package for tree-oriented workflows
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

`chattree hello` is not public CLI; it is a scaffold example leftover and must fail.

## Documentation

- Documentation home: https://arch.gh.wzhecnu.cn/ChatTree/
- CLI tree: https://arch.gh.wzhecnu.cn/ChatTree/cli-tree/
- English docs: https://arch.gh.wzhecnu.cn/ChatTree/en/

## Development Notes

Read `DEVELOP.md` and `AGENTS.md` before expanding commands, and keep `--tree`, README, MkDocs, tests, and changelog synchronized.
