"""
Presentation timer
"""
import math
import os
import sys
import time

def countdown(minutes=0):
    """
    Countdown for `minutes`

    Arguments:
    - `minutes`:
    """
    secs = minutes * 60
    try:
        while secs > 0:
            status = '{0} mins, {1} secs left!'.format(
                math.floor(secs / 60), secs % 60
                )
            os.system('clear')
            print(status)
            secs -= 1
            time.sleep(1)
        print("You're outta time!")
    except KeyboardInterrupt:
        print("Cancelled Early!")
        sys.exit(0)
