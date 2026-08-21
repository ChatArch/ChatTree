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
chattree --help
chattree --version
chattree --tree
chattree --tree-brief
```

开发环境：

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```

## CLI 树

ChatTree 使用共享的 `chatstyle.add_tree_option()` 从真实注册的 Click command surface 生成完整和简洁命令树。当前 CLI 是 root-only，因此两个视图的节点相同。

```text
chattree
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`chattree hello` 不是公开 CLI；它属于脚手架示例残留，必须失败。

## CLI 规范

- 根命令显式命名为 `chattree`，并暴露 `--version`、`--tree` 和 `--tree-brief`。
- `--tree` / `--tree-brief` 由 `chatstyle>=0.2.0,<0.3.0` 从真实 Click 注册面生成，不维护包内 renderer。
- 当前包没有 env/profile/config 行为，因此不依赖 ChatEnv；未来需要配置时，应注册 typed provider，并使用 `chatenv>=0.2.10,<0.3.0` 与 ChatEnv 管理的存储路径。
- 当前 root-only 入口只输出包与命令元数据，不读取或修改项目树，也不处理敏感值。

## 文档

- 文档首页：https://arch.gh.wzhecnu.cn/ChatTree/
- CLI 树：https://arch.gh.wzhecnu.cn/ChatTree/cli-tree/
- 英文文档：https://arch.gh.wzhecnu.cn/ChatTree/en/

## 开发说明

扩展命令前先阅读 `DEVELOP.md` 和 `AGENTS.md`，并保持 `--tree`、`--tree-brief`、README、MkDocs、测试与 changelog 同步。
