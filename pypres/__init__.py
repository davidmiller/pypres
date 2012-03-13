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
    parser.add_argument("-s", "--slide", help = "Start at slide num (0 indexed)", default = 0)
    args =  parser.parse_args()

    sys.ps1 = '{0}.{1} >>> '.format( *sys.version_info)
    replish = PresentConsole(args.presentation, slidenum=int(args.slide))
    replish.interact()

