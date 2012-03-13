import re

from distutils.core import setup

VERSION_FILE = "pypres/_version.py"
verstrline = open(VERSION_FILE, "rt").read()
VSRE = r'^__version__ = [\'"]([^\'"]*)[\'"]$'
mo = re.search(VSRE,  verstrline, re.M)
if mo:
    VERSION = mo.group(1)
else:
    print verstrline
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
        ],
    packages = ['pypres'],
    install_requires = []
    )
