# ChatTree

`ChatTree` is the ChatArch Python CLI package shell for tree-oriented workflows. The public CLI currently exposes package metadata and the real command tree only; future tree capabilities should start with reusable Python APIs before extending CLI commands, docs, and tests.

<div class="grid cards" markdown>

-   :material-console-line: **CLI Tree**

    ---

    Inspect the current real command surface: [`chattree --tree`](cli-tree.md).

-   :material-file-tree: **Tree Boundary**

    ---

    The current version is a lightweight entrypoint and does not read or mutate real project trees.

-   :material-shield-check: **Verification Contract**

    ---

    `--tree`, README, MkDocs, and tests must stay synchronized.

</div>

## Quick Start

```bash
pip install ChatTree
chattree --version
chattree --tree
```

## Development Verification

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```
