"""PyBug - python debugging utilities/extension of pdb

The intent of this code is that it would be either included directly or used as
an inspiration for features of the pdb module in the Python Standard Library.

Copyright (c) 2012 Daniel Miller

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import os
import sys
from pdb import Pdb

class Error(Exception): pass

def trace():
    """like pdb.set_trace() except sets a breakpoint for the next line
    
    works with nose testing framework (uses sys.__stdout__ for output)
    """
    frame = sys._getframe().f_back
    pdb = Pdb(stdout=sys.__stdout__)
    pdb.set_trace(frame)

def setbreak(line=None, file=None, cond=None, temp=0, frame=None, throw=False):
    """set a breakpoint or a given line in file with conditional
    
    arguments:
        line - line number on which to break
        file - module or filename where the breakpoint should be set
        cond - string with conditional expression, which (if given) must
            evaluate to true to break
        temp - if true, create a temporary breakpoint
    
    example usage:
    
        setbreak(42, "/path/to/universe.py", "name == 'hitchhiker'")
        setbreak(35, "package.module")

    see: http://groups.google.com/group/comp.lang.python/browse_thread/thread/103326200285cb07#
    """
    if frame is None:
        frame = sys._getframe().f_back
    if file is None:
        file = frame.f_code.co_filename
    elif not file.startswith("file:") and os.path.sep not in file:
        try:
            mod = __import__(file, globals(), locals(), ["__file__"])
        except ImportError, err:
            if throw:
                raise
            sys.__stdout__.write("cannot set breakpoint: %s:%s : %s" %
                (file, line, err))
            return
        file = mod.__file__
        sys.__stdout__.write("breaking in: %s" % file)
    if file.endswith(".pyc"):
        file = file[:-1]
    pdb = Pdb(stdout=sys.__stdout__) # use sys.__stdout__ to work with nose tests
    pdb.reset()
    pdb.curframe = frame
    while frame:
        frame.f_trace = pdb.trace_dispatch
        pdb.botframe = frame
        frame = frame.f_back
    templine = line
    while templine < line + 10:
        error = pdb.set_break(file, templine, cond=cond, temporary=temp)
        if error:
            templine += 1
        else:
            break
    if error:
        error = pdb.set_break(file, line, cond=cond, temporary=temp)
        if throw:
            raise Error(error)
        sys.__stdout__.write("\n%s\n" % error)
        return
    sys.__stdout__.write("\n")
    pdb.do_break("") # print breakpoints
    pdb.set_continue()
    sys.settrace(pdb.trace_dispatch)
