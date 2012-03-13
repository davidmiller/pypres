import re

from distutils.core import setup

VERSION_FILE = "pypres/_version.py"
verstrline = open(VERSION_FILE, "rt").read()
VSRE = r'^__version__ = [\'"]([^\'"]*)[\'"]$'
mo = re.search(VSRE,  verstrline, re.M)
if mo:
    VERSION = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in {0}".format(VERSION_FILE))

LONG_DESC = """
Make Python related presentations in a Python Repl!
"""
setup(
    name = "pypres",
    version = VERSION,
    author = "David Miller",
    author_email = "david@deadpansincerity.com",
    url = "https://github.com/davidmiller/pypres",
    description = "Presentation in a Python REPL",
    long_description = LONG_DESC,
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Communications",
        "Topic :: Education",
        "Topic :: Office/Business",
        "Topic :: Utilities"
        ],
    packages = ['pypres'],
    install_requires = []
    )
