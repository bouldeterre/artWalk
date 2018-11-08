import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="artWalk_pkg",
    version="0.0.1",
    author="Emonides Pierre-Emmanuel",
    author_email="pierreemmanuel.emonides@gmail.com",
    description="Wallpaper switcher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bouldeterre/artWalk",
    packages=setuptools.find_packages(),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
