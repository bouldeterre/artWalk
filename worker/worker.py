import click
from worker.PaintClient import PaintClient
from worker.config import setConfig, RIJKKEYPHRASE


def print_help_msg(command):
    with click.Context(command) as ctx:
        click.echo(command.get_help(ctx))


def internal_launch():
    try:
        with PaintClient() as cl:
            paint = cl.getRandomPaint()
            cl.printUrl(paint[2], paint[0])
    except Exception as e:
        print(e)
        print_help_msg(cli)


@click.group()
def cli():
    pass


@click.command(help="Run the Cli")
def launch():
    """ """
    internal_launch()


@click.command(help="Set your ApiKey")
@click.option(
    "--rijk-key", prompt=RIJKKEYPHRASE, hide_input=True, help="Rijksmuseum API key"
)
def config(rijk_key):
    """ """
    setConfig(rijk_key)


cli.add_command(launch)
cli.add_command(config)


if __name__ == "__main__":
    cli()
