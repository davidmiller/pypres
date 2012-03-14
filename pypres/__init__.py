"""
Let's make this a package!
"""
import argparse
import os
import sys

from pypres.pres import PresentConsole
from pypres.timer import countdown

def main():
    """
    OH: You want to run a program then?
    """
    parser = argparse.ArgumentParser(
        description = "Presenting"
        )
    subparsers =  parser.add_subparsers(title="commands")
    parser_run = subparsers.add_parser("run", help="Run the presentation")
    parser_run.add_argument("presentation",  help = "Presentation file to run")
    parser_run.add_argument("-s", "--slide", help = "Start at slide num (0 indexed)", default = 0)
    parser_run.set_defaults(func=pres)
    parser_time = subparsers.add_parser("time", help="aCountdown timer for presentations")
    parser_time.add_argument("minutes", help="Minutes to count down")
    parser_time.set_defaults(func=timer)

    args =  parser.parse_args()
    args.func(args)

def pres(args):
    """
    Run the presentation
    """
    sys.ps1 = '{0}.{1} >>> '.format( *sys.version_info)
    os.system("clear")
    replish = PresentConsole(args.presentation, slidenum=int(args.slide))
    replish.interact()

def timer(args):
    """
    Time a presentation
    """
    countdown(int(args.minutes))
