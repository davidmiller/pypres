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
    def __init__(self, prespath, slidenum=0, *args, **kwargs):
        self._prespath = prespath
        self._slidenum = slidenum
        code.InteractiveConsole.__init__(self, *args, **kwargs)
        with open(prespath, 'r') as presfile:
            self.slides = presfile.read().split("#--newslide")

    def statusing(self):
        """
        Print the status of our presentation
        """
        status = "Slide {0} of {1}".format(self._slidenum, len(self.slides))
        print(status)
        return

    def codeslide(self, slide):
        """
        Runs a slide with some code in it.

        Arguments:
        - `slide`: str
        """
        stripped = slide[7:].strip()
        for x in stripped.split("\n"):
            print(sys.ps1 + x)
            super(PresentConsole, self).push(x)
        return

    def simpleslide(self, slide):
        """
        This is text rite? I guess we'll just print() it

        Arguments:
        - `slide`: str
        """
        print(slide)
        return

    def splitslide(self, slide):
        """
        This slide wants to get printed bit by bit.

        Let's do that.

        Arguments:
        - `slide`:
        """
        slide = slide.strip()
        sections = slide[8:].split('#----')
        for i, section in enumerate(sections):
            if section == '':
                continue
            print(section.strip())
            if i + 1 < len(sections):
                input = self.raw_input()
                if input != '':
                    raise ValueError("Entered code in a splitside. Stop it.")
        return

    def prevslide(self):
        """
        Go back one slide!
        """
        self._slidenum -= 2
        return self.runslide("")

    def runslide(self, line):
        """
        Print then run a slide
        """
        if self._slidenum >= len(self.slides):
            return
        os.system('clear')
        if line.strip() == "^":
            return self.prevslide()
        else:
            slide =  self.slides[self._slidenum].strip()
            self._slidenum += 1
        self.statusing()
        if slide.startswith("#--code"):
            return self.codeslide(slide)
        if slide.startswith('#--split'):
            return self.splitslide(slide)
        return self.simpleslide(slide)

    def push(self, line):
        """
        If we're passed an empty string, get the next part of the presentation
        """
        if line == "" or line == "^":
            return self.runslide(line)
        return super(PresentConsole, self).push(line)
