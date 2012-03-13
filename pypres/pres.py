"""
A presentation about Python!
"""
import code
import os
import sys

class PresentConsole(code.InteractiveConsole):
    """
    A console that models the Python interpreter except...

    Empty newlines execute the next block of python code...
    """
    def __init__(self, prespath, *args, **kwargs):
        self._prespath = prespath
        self._slidenum = 0
        code.InteractiveConsole.__init__(self, *args, **kwargs)
        with open(prespath, 'r') as presfile:
            self.slides = presfile.read().split("#--newslide")

    def runslide(self, line):
        """
        Print then run a slide
        """
        try:
            os.system('clear')
            #import pdb; pdb.set_trace()
            if line.strip() == "^":
                slide = self.slides[self._slidenum - 1].strip()
                self._slidenum -= 1
            else:
                slide =  self.slides[self._slidenum].strip()
                self._slidenum += 1
            if slide.startswith("#--code"):
                print(sys.ps1 + slide[7:].strip())
                return super(PresentConsole, self).push(slide)
            print(slide)
        except IndexError: # No more slides
            if self._slidenum != len(self.slides):
                raise
        return


    def push(self, line):
        """
        If we're passed an empty string, get the next part of the presentation
        """
        if line == "" or line == "^":
            return self.runslide(line)
        return super(PresentConsole, self).push(line)
