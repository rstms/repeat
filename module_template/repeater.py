# -*- coding: utf-8 -*-
"""repeater object for repeat command line tool

This simple module contains a Repeater() class with a run() method that
does the work of the program.

Example:
    To use the function open an input stream and an output stream in text 
    mode, then cal the run method specifying the number of times to repeat
    the copy of the input.
    To use it from Python code::

        >>> form repeat import Repeater
        >>> Repeater(sys.stdin, sys.stdout, 1).run()

The function operates in text mode and uses line buffering. It is designed
to be called by the click api.
"""

import io
import tempfile
import sys

from .exception import ParameterError


class Repeater():
    """Repeat stream input to output mutliple times"""

    def __init__(self):
        """Context constructor"""
        pass

    def run(self, infile, outfile, count=1, prefix=False):
        """Copy stdin to stdout and a buffer, then output the buffer multiple times.

        Arguments
            infile (:obj: `File`): input file
            outfile (:obj: `File`): output file
            count (int): number of output repetitions
            prefix (bool): begin output with line count
        """

        if count < 0:
            raise ParameterError('I refuse to repeat a negative number of times.')

        # see if the stream is binary or text
        if isinstance(infile, io.TextIOBase):
            mode = 'w+'
        else:
            mode = 'wb+'

        buf = tempfile.SpooledTemporaryFile(mode=mode)
        for (length, line) in enumerate(infile):
            buf.write(line)
        if prefix:
            outfile.write(f'{length+1}\n')
        for _ in range(0, count):
            buf.seek(0)
            for line in buf:
                outfile.write(line)
