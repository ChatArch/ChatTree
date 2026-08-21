"""CLI entrypoint for chattree."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chattree import __version__


@click.group(
    name="chattree",
    invoke_without_command=True,
    no_args_is_help=True,
)
@click.version_option(__version__, prog_name="chattree")
@add_tree_option(renderer_options={"root_name": "chattree"})
def main() -> None:
    """ChatTree placeholder package for tree-oriented workflows."""
    pass


if __name__ == "__main__":
    main()
