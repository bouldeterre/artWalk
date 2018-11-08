
![WalkWalk](walk.jpg)

- worker Fetch art from X API
- cli Apply the Wallpaper

##### Dependencies

    # Poetry
    pip3 install poetry

    # Packages
    poetry install

#### Quickstart

    python launch.py

Or separately


    python -m worker.worker config
    python -m worker.worker launch
    python -m WallpaperCli.cli launch

#### Run CLI Demo
No needs for API KEY, this will use local files

    python -m WallpaperCli.cli test


“... was developed using the [Rijksmuseum API](https://rijksmuseum.github.io/)
”
