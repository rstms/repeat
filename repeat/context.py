# -*- coding: utf-8 -*-
"""context object for repeat command line tool

This module contains the application object attached to the click ctx object.
It maintains the state of command line switches and serves as a connection
point between multiple commands in a multi-level cli application.  It
implements an exception handler to display single line error messages
that are more generally expected from CLI programs, and takes a boolean
debug option that selects standard exception handling if desired.

In this simple program it also contains a run method that does the work of the 
program.

Example:
    To use the function open an input stream and an output stream in text 
    mode, then cal the run method specifying the number of times to repeat
    the copy of the input.
    To use it from Python code::

        >>> import repeat, sys
        >>> c = Context().run(sys.stdin, sys.stdout, 1)

The function operates in text mode and uses line buffering. It is designed
to be called by the click api.


Todo:
    * binary mode i/o
"""

import tempfile
import sys


class Context():
    """Context singleton object represents the state of the application.  

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        quiet (bool): suppress non-error output
        verbose (bool): provide more extensive diagnostic output
        debug (bool): select the default exception handler if true
    """

    def __init__(self, quiet, verbose, debug, handler):
        """Context constructor"""
        self.quiet = quiet
        self.verbose = verbose
        self.debug = debug

        def exception_handler(exception_type,
                              exception,
                              traceback,
                              debug_hook=sys.excepthook):
            """handle runtime exceptions based on debug flag"""
            if debug:
                debug_hook(exception_type, exception, traceback)
            else:
                if verbose:
                    message = str(exception)
                else:
                    message = str(exception).split('\n')[0]
                handler(f"{exception_type}.{message}")
            sys.exit(-1)

        sys.excepthook = exception_handler

    def run(self, fin, fout, count):
        """Copy stdin to stdout and a buffer, then output the buffer multiple times.
       
        Arguments:
            fin (:obj:File): input stream
            out (:obj:File): output stream
            count (int): number of repetitions
        """
        buf = tempfile.SpooledTemporaryFile()
        for line in fin:
            buf.write(line)
            fout.write(line)

        for _ in range(0, count):
            buf.rewind()
            for line in buf():
                fout.write(buf)
