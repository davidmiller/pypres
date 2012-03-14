#!/usr/bin/env python3
"""

Python 3 for fun and profit




David Miller <david@deadpansincerity.com>
@thatdavidmiller



"""
#--newslide
"""



Python 3? FTWLarry?



"""
#--newslide
"""



Python 3 - it's the *future*



"""
#--newslide
"""
PEP 404: Python 2.8 Un-release Schedule

Quotes:

Un-release Schedule

The current un-schedule is:

2.8 final Never
Official pronouncement

Rule number six: there is no official Python 2.8 release.
There never will be an official Python 2.8 release.
It is an ex-release.
Python 2.7 is the end of the Python 2 line of development.

Upgrade path

The official upgrade path from Python 2.7 is to Python 3.

http://www.python.org/dev/peps/pep-0404/
"""
#--newslide
"""


Larry: what is this Python 3 thing then?



"""
#--newslide
"""
Quotes:

Python 3.0, also known as “Python 3000” or “Py3K”, is the first ever intentionally
backwards incompatible Python release.
Nevertheless, after digesting the changes, you’ll find that Python really hasn’t
changed all that much – by and large, we’re mostly fixing well-known annoyances
and warts, and removing a lot of old cruft.

http://docs.python.org/release/3.0.1/whatsnew/3.0.html
"""
#--newslide
"""

Larry: So, what's  changed?

"""
#--newslide
"""

Print is a function now!

http://www.python.org/dev/peps/pep-3105/

"""
#--newslide
#--code
print("Hello Beautiful World!")
#--newslide
#--code
print "Hello Beautiful World!"
#--newslide
"""



Strings:

* All strings are Unicode.



"""
#--newslide
"""

That's right Larry, u'My Unicode string'

Is no longer a thing.

"""
#--newslide
"""

In Python 3 we Unicode All The Strings.

"""
#--newslide
#--code
unicode_str = 'This is Unicode Larry!'
print(unicode_str, unicode_str.__class__)
#--newslide
"""

If you actually *want* a Bucket of Bytes, we have Bytes literals for you...

"""
#--newslide
#--code
bucket = b'This is a Bucket of Bytes Larry!'
print(bucket, bucket.__class__)
#--newslide
"""

Larry: 'WHY WOULD YOU DO THAT? '
Larry: 'YOU JUST BROKE ALL MY CODEZ!'

"""
#--newslide
#--split
"""
Previously, if your Unicodez happend to contain only 7-bit (ASCII) bytes...
"""
#----
"""
... and you tried to concatenate it with a Python 2.x str type...
"""
#----
"""
... Python would try to do the Right Thing
"""
#--newslide
#--split
"""
This used to work:

mystr = u'\u00A3'+ ' 2.99' + ' cheap!'
"""
#----
"""
Yes Larry, for those of you who don't know your Unicodez by heart,
That's the Unicode for a Pound Sign...
"""
#----
"""
Now However...
"""
#--newslide
#--code
price = '\u00A3 2.99' + b' cheap'
#--newslide
"""

Now you have to convert bytes to Unicode if you want to deal with them like text

"""
#--newslide
#--code
comment = b' cheap'
price = '\u00A3 2.99' + comment.decode()
print(price)
#--newslide
"""
Quotes:

'This value-specific behavior has caused numerous sad faces over the years.'

-Guido van Rossum February 14, 2009
"""
#--newslide
"""



You had a list, now you have a view!



"""
#--newslide
#--split
"""
Larry: Great.
"""
#----
"""
Larry: What in the world is a view?
"""
#----
"""
OH: It's a generator. We're cool.
"""
#--newslide
#--code
map(lambda x: x ** 10, range(10))
filter(lambda x: x > 3, range(10))
#--newslide
"""
Incidentally, you are encouraged *not* to map

Quotes:

a better fix is often to use a list comprehension
(especially when the original code uses lambda), or rewriting the code so it
doesn’t need a list at all. Particularly tricky is map() invoked for the side
effects of the function; the correct transformation is to use a regular for
loop (since creating a list would just be wasteful).

http://docs.python.org/release/3.0.1/whatsnew/3.0.html

"""
#--newslide
#--code
somedict = {'foo': 1, 'bar': 2, 'car': 3}
somedict.keys()
somedict.items()
somedict.values()
#--newslide
#--split
"""
While we're on the topic of dicts...
"""
#----
"""
U can haz dict comprehensions!

http://www.python.org/dev/peps/pep-0274/
"""
#--newslide
#--code
{i : chr(65+i) for i in range(4)}
#--newslide
#--split
"""
While we're on the topic of range...
"""
#----
"""
xrange is no longer a thing...
"""
#--newslide
#--code
xrange(0, 1000000)
#--newslide
#--split
"""

Instead, range returns a generator

"""
#----
"""
Er, I mean view
"""
#--newslide
#--code
range(0, 4)
#--newslide
"""

Starargs argument unpacking

frist, *rest= sometuple

"""
#--newslide
#--code
somenums = [1, 2, 3, 4, 5, 6, 7]
# Python 2.x way:
frist,  second,  rest = (lambda a, b, *r: (a, b, r))(*somenums)
print(frist, second, rest, sep="\n")
#--newslide
#--code
# python 3.x way:
frist, second, *rest = somenums
print(frist, second, rest, sep="\n")
#--newslide
#--split
"""
Argparse is in the stdlib!
"""
#----
"""
Argparse is *awesome*
"""
#--newslide
"""

Python 3.3 (probably) will have virtualenv built in!

https://bitbucket.org/vinay.sajip/pythonv


"""
#--newslide
"""


Porting your codez!


"""
#--newslide
"""


2to3 is here to help!


"""
#--newslide
"""

2to3 takes your Python 2.x codez and makes them Python3 codez!

"""
#--newslide
"""
david@bosch:~/src/dist/pypres$ 2to3 --help
Usage: 2to3 [options] file|dir ...

Options:
  -h, --help            show this help message and exit
  -d, --doctests_only   Fix up doctests only
  -f FIX, --fix=FIX     Each FIX specifies a transformation; default: all
  -j PROCESSES, --processes=PROCESSES
                        Run 2to3 concurrently
  -x NOFIX, --nofix=NOFIX
                        Prevent a transformation from being run
  -l, --list-fixes      List available transformations
  -p, --print-function  Modify the grammar so that print() is a function
  -v, --verbose         More verbose logging
  --no-diffs            Don't show diffs of the refactoring
  -w, --write           Write back modified files
  -n, --nobackups       Don't write backups for modified files

"""
#--newslide
#--split
"""
or...
"""
#----
"""

You can run 2.6 -> trunk in a single codebase

"""
#----
"""
Mostly.
"""
#--newslide
"""


Why would you do this?


"""
#--newslide
#--split
"""
Advantages:
"""
#----
"""
It's a single codebase.
"""
#----
"""
No 2to3 compilation step.
"""
#----
"""
Line numbers in tracebacks are canonical.
"""
#--newslide
"""

Great.
How do I do this?

"""
#--newslide
"""

You can just import the __future___

"""
#--newslide
#--code
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
#--newslide
#--split
"""
But...
"""
#----
"""
This means that your whole source file has basic python semantics altered...
"""
#----
"""
This can be a Bad Thing.
"""
#--newslide
#--split
"""
Like the answer to all interesting questions...
"""
#----
"""
... it depends.
"""
#--newslide
"""

If you're doing proper code review, crack on.

You can enforce it.

"""
#--newslide
"""

*Apparently* it can be a distraction for projects with lots of contributors from...

... interesting sources

"""
#--newslide
#--split
"""
Oh: Remember what I said about u'some unicode string' not being a thing?
"""
#----
"""
It wasn't "entirely" "true"
"""
#--newslide
"""

Unicode literals are *back*!

http://www.python.org/dev/peps/pep-0414/

"""
#--newslide
#--split
"""
It comes from the Python web community
"""
#----
"""
Who were largely doing Unicode right *anyway*
"""
#--newslide
#--split
"""
It will go into Python 3.3
"""
#----
"""
Probably.
"""
#----
"""
Quotes:

BDFL Pronouncement

This PEP has been formally accepted for Python 3.3:

I'm accepting the PEP. It's about as harmless as they come. Make it so.
"""
#--newslide
"""
Which means that as of 3.3, if you're doing Unicode properly for Python 2.6 >

Your code has a great chance of being easy to port.
"""
#--newslide
#--split
"""
Six
"""
#----
"""
Because:
2 * 3 == six rite?
"""
#----
"""
http://pypi.python.org/pypi/six/
http://packages.python.org/six/ (Docs)
"""
#--newslide
#--split
"""
Six is pretty awesome
"""
#----
"""
(Because) it's quite simple really
"""
#----
"""
It's jsut a wrapper around common compatibility problems
"""
#--newslide
#--code
import six
six.u("Some Unicode")
six.b("Some Bytes")
#--newslide
#--code
from six.moves import StringIO
StringIO
#--newslide
#--split
"""
my_cool_library = raw_input()
"""
#----
"""
Larry: But what about my_cool_library?
Larry: Is it ported yet?
"""
#----
"""
http://getpython3.com/#notable-ports
"""
#--newslide
"""
Pyramid 1.3a1
Django (Development Branch)
Mako Templates
SQLAlchemy
Webob
lxml
pip
virtualenv
celery
python-dbus
requests
"""
#--newslide
"""
But what about my_cool_library?
"""
#--newslide
#--split
"""
So just port it already!
"""
#----
"""
It's mostly not that hard...
"""
#----
"""
For varying values of $hard
"""
#----
"""
But...
"""
#--newslide
#--split
"""
The PSF will happily fund porting sprints

http://pythonsprints.com/
"""
#----
"""
So just port it already!
"""
#--newslide
"""


Invaluable resources (3)

http://docs.python.org/release/3.0.1/whatsnew/3.0.html

http://diveintopython3.ep.io/

http://docs.python.org/py3k/howto/pyporting.html



"""
#--newslide
"""

That's all folks !

Only thing left is $PROFIT

But I guess we're out of time...

"""
#--newslide
"""

Python 3 for fun and profit




David Miller <david@deadpansincerity.com>
@thatdavidmiller



"""
