from setuptools import setup, find_packages

setup(
    name="Hell Spider",
    version="0.0.1",
    description="""
    A multi-functional recon, exploitation and post-exploitation tool
    """,
    url="https://www.github.com/GhettoCole/Hell-Spider-Hackers-Tool-",
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
