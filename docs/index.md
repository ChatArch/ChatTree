# ChatTree

`ChatTree` 是 ChatArch tree-oriented workflows 的 Python CLI 包壳。当前公开 CLI 只提供包信息与真实命令树；后续新增 tree 能力时，应先落到可复用 Python API，再扩展 CLI、文档和测试。

<div class="grid cards" markdown>

-   :material-console-line: **CLI 树**

    ---

    查看当前真实命令面：[`chattree --tree`](cli-tree.md)。

-   :material-file-tree: **Tree 边界**

    ---

    当前版本是轻量入口，不读取或修改真实项目树。

-   :material-shield-check: **验证契约**

    ---

    `--tree`、README、MkDocs 和测试必须同步更新。

</div>

## 快速开始

```bash
pip install ChatTree
chattree --version
chattree --tree
```

## 开发验证

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```
