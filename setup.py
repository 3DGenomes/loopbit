import os
from setuptools import setup, find_packages, Command


__version__ = None
exec(open('loopbit/version.py').read())

class CleanCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info ./htmlcov')

setup(
    name='loopbit',
    version=__version__,
    description='Loop caller from 3C based experiments.',
    url='https://github.com/3DGenomes/loopbit',
    setup_requires=[
        'setuptools>=18.0',
    ],
    packages=find_packages(),
    install_requires=[
        'cython',
        'tensorflow',
        'seaborn',
        'keras',
        'numpy==1.14.5',
        'matplotlib',
        'scipy',
        'pandas',
    ],
    scripts=['bin/loopbit'],
    cmdclass={
        'clean': CleanCommand
    },
    classifiers=(
        "Programming Language :: Python :: 3.",
    ),
)
