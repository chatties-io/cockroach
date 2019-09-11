"""Entry point."""

import click

from . import __version__, hello


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__)
def cli():
    """Scrap news websites for statistics on words."""
    hello()


def main():
    """Entry point."""
    cli(auto_envvar_prefix="COCKROACH")


if __name__ == "__main__":
    main()
