"""
Let's make this a package!
"""
import argparse
import sys

from pypres.pres import PresentConsole

def main():
    """
    OH: You want to run a program then?
    """
    parser = argparse.ArgumentParser(
        description = "Presenting"
        )
    parser.add_argument("presentation",  help = "Presentation file to run")
    args =  parser.parse_args()

    sys.ps1 = '{0}.{1} >>> '.format( *sys.version_info)
    replish = PresentConsole(args.presentation)
    replish.interact()

