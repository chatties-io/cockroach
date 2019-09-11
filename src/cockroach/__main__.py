"""Entry point."""

import asyncio
import os

import aiohttp
import click
import sqlalchemy
import sqlalchemy.orm

from . import __version__, hello, german, models

async def async_check(word):
    """Scrap news websites for statistics on words."""
    async with aiohttp.ClientSession() as session: 
        if await german.check_word(session, word):
            click.echo(
                click.style(f"The word {word} is a german one.", fg="green"))
        else:
            click.echo(
                click.style(f"The word {word} is *NOT* a german one.",
                            fg="red"))


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__)
@click.pass_context
def cli(ctx):
    pass


@cli.command()
@click.argument("url")
def add_rss(url):
    """Add an RSS stream to the database."""


@cli.command("create-db")
def create_db():
    """Create the database."""
    engine = sqlalchemy.create_engine(os.environ['COCKROACH_DATABASE'])
    session = sqlalchemy.orm.sessionmaker()
    session.configure(bind=engine)
    models.Base.metadata.create_all(engine)
    click.echo("Database created!")


@cli.command()
@click.argument("word")
def async_check(word):
    """Check whether a word is german or not."""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_cli(word))


def main():
    """Entry point."""
    cli(auto_envvar_prefix="COCKROACH")


if __name__ == "__main__":
    main()
