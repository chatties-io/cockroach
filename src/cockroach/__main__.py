"""Entry point."""

import asyncio

import aiohttp
import click

from . import __version__, hello, german

async def async_cli(word):
    """Scrap news websites for statistics on words."""
    async with aiohttp.ClientSession() as session: 
        if await german.check_word(session, word):
            click.echo(
                click.style(f"The word {word} is a german one.", fg="green"))
        else:
            click.echo(
                click.style(f"The word {word} is *NOT* a german one.",
                            fg="red"))


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__)
@click.argument("word")
def cli(word):
    """Scrap news websites for statistics on words."""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_cli(word))


def main():
    """Entry point."""
    cli(auto_envvar_prefix="COCKROACH")


if __name__ == "__main__":
    main()
