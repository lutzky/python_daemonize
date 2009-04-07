from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='python_daemonize',
      version=version,
      description="Simple daemonization utility based on BSD daemon(3)",
      long_description="""Simple daemonization utility based on BSD daemon(3)

Usage from within python:
- import daemonize
- run daemonize.daemon() at the appropriate time

Usage from the shell:
daemonize.py [path] [arguments]

Note that [path] has to be a full path to an executable file

Ported from Brian Clapper's daemonize at
http://www.clapper.org/software/daemonize/
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='daemon daemonize',
      author='Ohad Lutzky',
      author_email='ohad@lutzky.net',
      url='http://github.com/lutzky/python_daemonize',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
        'console_scripts': [
            'daemonize = python_daemonize.daemonize:main',
        ],
      },
      )
