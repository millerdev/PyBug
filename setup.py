from distutils.core import setup

setup(
    name='PyBug',
    version='1.0',
    author='Daniel Miller',
    keywords='debug pdb extension',
    url='http://github.com/millerdev/PyBug',
    description=open('README.md').read(),
    py_modules=['bug'],
)
