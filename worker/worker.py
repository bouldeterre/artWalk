import asyncio
import aiohttp
import click
import os
import json


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "http://python.org")
        print(html)


@click.group()
def cli():
    pass


@click.command()
def launch():
    """ """
    print("Launch Worker")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


@click.command()
@click.option(
    "--rijk-key",
    prompt="What is your Rijksmuseum API key(https://www.rijksmuseum.nl/en/api)",
    hide_input=True,
)
def config(rijk_key):
    """ """
    passfile = open(".artkeys", "w")

    data = {"rijkkey": rijk_key}

    passfile.write(json.dumps(data))
    passfile.close()
    click.echo("Config ok")


cli.add_command(launch)
cli.add_command(config)


if __name__ == "__main__":
    cli()
