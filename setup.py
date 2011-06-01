from setuptools import setup

import eventer

setup(
    name='eventer',
    version=eventer.__version__,
    description='A simple event dispatching library',
    long_description=eventer.__doc__,
    author='Anand Chitipothu',
    author_email='anand@archive.org',
    py_modules=["eventer"],
    license="GPL v3"
)
