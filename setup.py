from setuptools import setup, find_packages

setup(
        name="WEB BOT",
        version="0.0.1",
        description="Multi-function Web-Bot",
        url="https://www.github.com/GhettoCole/Web-Bot/",
        license="GNU",
        author="Given Lepita",
        author_email="given.lepita@gmail.com",
        packages=find_packages(),
        install_requires=[
            "prettytable", "bs4", "requests",
        ],
        entry_points={},
        extras_require={},
)
