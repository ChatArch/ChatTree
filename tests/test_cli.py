from click.testing import CliRunner

from chattree import __version__
from chattree.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chattree, version {__version__}" in result.output


def test_top_level_help_exposes_tree_and_not_scaffold_hello():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "--tree" in result.output
    assert "hello" not in result.output.lower()


def test_tree_option_renders_truthful_root_only_surface():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0
    assert "chattree  # ChatTree placeholder package for tree-oriented workflows" in result.output
    assert "├── --help  # show command help" in result.output
    assert "├── --version  # show the installed package version" in result.output
    assert "└── --tree  # show this CLI tree" in result.output
    assert "hello" not in result.output.lower()


def test_scaffold_hello_command_is_not_public():
    result = CliRunner().invoke(main, ["hello", "ChatArch"])

    assert result.exit_code != 0
    assert "No such command" in result.output
