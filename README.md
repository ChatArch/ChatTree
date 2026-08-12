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

[英文版](README.en.md) | 简体中文
</div>

# ChatTree

`ChatTree` 是 ChatArch tree-oriented workflows 的 Python CLI 包壳。当前公开 CLI 只提供真实 root-only 包信息入口；后续新增 tree 能力时，必须同步 Python API、CLI 树、文档和测试。

## 快速开始

```bash
pip install ChatTree
chattree --version
chattree --tree
```

开发环境：

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```

## CLI 树

```text
chattree  # ChatTree placeholder package for tree-oriented workflows
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

`chattree hello` 不是公开 CLI；它属于脚手架示例残留，必须失败。

## 文档

- 文档首页：https://arch.gh.wzhecnu.cn/ChatTree/
- CLI 树：https://arch.gh.wzhecnu.cn/ChatTree/cli-tree/
- 英文文档：https://arch.gh.wzhecnu.cn/ChatTree/en/

## 开发说明

扩展命令前先阅读 `DEVELOP.md` 和 `AGENTS.md`，并保持 `--tree`、README、MkDocs、测试与 changelog 同步。
