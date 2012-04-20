import os.path
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='PyBug',
    version='1.0',
    author='Daniel Miller',
    author_email='millerdev@gmail.com',
    keywords='debug pdb extension',
    url='http://github.com/millerdev/PyBug',
    description=("PyBug extends Python's interactive debugger (pdb), making "
        "it simpler to add breakpoints to your code."),
    long_description=read('README.md'),
    py_modules=['bug'],
)
