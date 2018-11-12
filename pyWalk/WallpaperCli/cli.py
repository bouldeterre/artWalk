import click
import ctypes
import os
import glob
import random


def setWallpaper(fullpath):
    SPI_SETDESKWALLPAPER = 0x14  # SPI_SETDESKWALLPAPER command (20)
    SPIF_UPDATEINIFILE = 0x2  # forces instant update
    try:
        ret = ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER, 0, fullpath, SPIF_UPDATEINIFILE
        )
        print(f"Wallpaper Changed:{ret}")
    except Exception as e:
        print(e)
        raise


def internal_launch():
    print("Launch WallpaperCli")
    curpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    globpath = os.path.join(curpath, "assets/*_*.jpg")
    testfiles = glob.glob(globpath)
    fullpath = os.path.join(curpath, testfiles[-1])
    print(fullpath)
    setWallpaper(fullpath)


@click.group()
def cli():
    pass


@click.command()
def launch():
    """ """
    internal_launch()


@click.command()
def test():
    print("start test")

    curpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testfiles = glob.glob("assets/*.jpg")
    filename = random.choice(testfiles)

    fullpath = os.path.join(curpath, filename)
    print(fullpath)
    setWallpaper(fullpath)


cli.add_command(launch)
cli.add_command(test)

if __name__ == "__main__":
    cli()
