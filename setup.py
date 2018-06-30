import os.path
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='PyBug',
    version='1.2.1',
    author='Daniel Miller',
    author_email='millerdev@gmail.com',
    keywords='debug pdb extension',
    url='http://github.com/millerdev/PyBug',
    description=("PyBug extends Python's interactive debugger (pdb), making "
        "it simpler to add breakpoints to your code."),
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    py_modules=['bug'],
)
