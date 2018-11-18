import click
import ctypes
import os
import glob
import random
import subprocess

from sys import platform


def win32Wallpaper(fullpath):
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


def darwinWallpaper(fullpath):
    SCRIPT = """/usr/bin/osascript<<END
    tell application "Finder"
    set desktop picture to POSIX file "%s"
    end tell
    END"""

    try:
        ret = subprocess.Popen(SCRIPT % fullpath, shell=True)
        print(f"Wallpaper Changed:{ret}")
    except Exception as e:
        raise


def setWallpaper(fullpath):
    if platform == "linux" or platform == "linux2":
        # linux
        print("Linux not supported")
    elif platform == "darwin":
        # OS X
        darwinWallpaper(fullpath)
    elif platform == "win32":
        win32Wallpaper(fullpath)


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
