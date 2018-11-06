import click
from worker.PaintClient import PaintClient


def print_help_msg(command):
    with click.Context(command) as ctx:
        click.echo(command.get_help(ctx))


@click.group()
def cli():
    pass


@click.command(help="Run the Cli")
def launch():
    """ """
    print("Launch Worker")

    try:
        with PaintClient() as cl:
            paint = cl.getRandomPaint()
            # print("getRandomPaintName:".format())
            # cl.getPaint("SK-C-5")
            cl.printUrl(paint[2], paint[0])
    except Exception as e:
        print(e)
        print_help_msg(cli)


@click.command(help="Set your ApiKey")
@click.option(
    "--rijk-key",
    prompt="What is your Rijksmuseum API key(https://www.rijksmuseum.nl/en/api [Using the API's])",
    hide_input=True,
    help="Rijksmuseum API key",
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
