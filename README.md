PyBug - python debugging utilities
==================================

PyBug extends Python's interactive debugger (pdb), making it simpler to add
breakpoints to your code.

Usage examples:

    # Like pdb.set_trace(), but shorter :) and works with nosetests.
    import bug; bug.trace()

    # Set a breakpoint at line 35 of package.module
    bug.setbreak(35, "package.module")

    # Set a conditional breakpoint at line 42 of /path/to/universe.py
    bug.setbreak(42, "/path/to/universe.py", "name == 'hitchhiker'")

There are two notable features here that would ideally make it into the pdb
module in the Python Standard Library:

  * Easily set a breakpoint at an arbitrary line in an arbitrary module. This
    is useful when debugging a third-party library where the code cannot easily
    be edited to add a set_trace() call.

  * Set a breakpoint in a module named by import path rather than file path.

