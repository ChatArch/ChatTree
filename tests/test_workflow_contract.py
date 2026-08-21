from pathlib import Path

from chatstyle import render_click_tree

from chattree.cli import main

ROOT = Path(__file__).resolve().parents[1]


def _text_blocks(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [chunk.split("```", 1)[0].rstrip() for chunk in text.split("```text\n")[1:]]


def test_runtime_and_docs_dependency_contract():
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")

    assert '"click>=8.0,<9.0"' in pyproject
    assert '"chatstyle>=0.2.0,<0.3.0"' in pyproject
    assert '"mkdocs-material>=9.5,<9.7"' in pyproject
    assert "chatenv" not in pyproject


def test_publish_workflow_is_tag_only_oidc_and_main_guarded():
    workflow = (ROOT / ".github" / "workflows" / "publish.yml").read_text(encoding="utf-8")

    assert "tags:" in workflow
    assert "workflow_dispatch" not in workflow
    assert "id-token: write" in workflow
    assert "pypa/gh-action-pypi-publish@release/v1" in workflow
    assert "git fetch --no-tags origin main:refs/remotes/origin/main" in workflow
    assert 'git merge-base --is-ancestor "${GITHUB_SHA}" refs/remotes/origin/main' in workflow
    legacy_secret_markers = ["PYPI" + "_API_TOKEN", "TWINE" + "_PASSWORD", "secrets" + ".PYPI"]
    assert all(marker not in workflow for marker in legacy_secret_markers)


def test_docs_workflows_use_chatarch_site_url():
    preview = (ROOT / ".github" / "workflows" / "preview.yaml").read_text(encoding="utf-8")
    deploy = (ROOT / ".github" / "workflows" / "deploy.yaml").read_text(encoding="utf-8")
    ci = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")

    assert "CHATARCH_PREVIEW_URL" in preview
    assert "site_url=$(python" in preview
    assert "mkdocs.yml" in preview
    assert "github.io" not in preview
    assert "mkdocs gh-deploy --force" in deploy
    assert "mkdocs build --strict" in ci
    assert "chattree --tree" in ci


def test_ci_checks_installed_full_and_brief_trees_and_distributions():
    workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")

    assert 'python-version: ["3.10", "3.11", "3.12"]' in workflow
    assert "chattree --version" in workflow
    assert "chattree --tree" in workflow
    assert "chattree --tree-brief" in workflow
    assert "python -m build" in workflow
    assert "python -m twine check dist/*" in workflow
    assert '"$RUNNER_TEMP/chattree-wheel/bin/python" -m pip install dist/*.whl' in workflow


def test_mkdocs_material_renderer_and_public_domain():
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    assert "site_url: https://arch.gh.wzhecnu.cn/ChatTree/" in config
    assert "pymdownx.emoji" in config
    assert "material.extensions.emoji.twemoji" in config
    assert "material.extensions.emoji.to_svg" in config
    assert "cli-tree.md" in config


def test_public_docs_expose_full_and_brief_tree_commands():
    checked = [
        ROOT / "README.md",
        ROOT / "README.en.md",
        ROOT / "docs" / "index.md",
        ROOT / "docs" / "index.en.md",
        ROOT / "docs" / "cli-tree.md",
        ROOT / "docs" / "cli-tree.en.md",
    ]
    for path in checked:
        text = path.read_text(encoding="utf-8")
        assert "chattree --tree" in text, path
        assert "chattree --tree-brief" in text, path


def test_bilingual_cli_tree_docs_match_registered_full_and_brief_trees():
    expected = [
        render_click_tree(main, root_name="chattree"),
        render_click_tree(main, root_name="chattree", brief=True),
    ]

    for path in (ROOT / "docs" / "cli-tree.md", ROOT / "docs" / "cli-tree.en.md"):
        text = path.read_text(encoding="utf-8")
        assert "chatstyle.add_tree_option()" in text
        assert _text_blocks(path)[:2] == expected
