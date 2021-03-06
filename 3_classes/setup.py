"""
mdsim
A Simple Molecular Dynamics Simulation Package
"""
from setuptools import setup, find_packages

DOCLINES = __doc__.split("\n")

setup(
    name='mdsim',
    author='Yudong Qiu',
    description=DOCLINES[0],
    long_description="\n".join(DOCLINES[2:]),
    version=0.1,
    packages=find_packages(),
    url='https://github.com/lpwgroup/programming-tutorial/',
    install_requires=[
        'numpy>=1.11',
        'pytest'
    ]
)
