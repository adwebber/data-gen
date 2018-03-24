#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for data_gen.

    This file was generated with PyScaffold 3.0.2.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: http://pyscaffold.org/
"""

import sys
from setuptools import setup

# Add here console scripts and other entry points in ini-style format
entry_points = """
[console_scripts]
data_gen = data_gen.runner:run
"""


def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    setup_requires = ['pytest-runner']
    if needs_sphinx:
        setup_requires.append('sphinx')

    setup(
        version='v0.1',
        setup_requires=setup_requires,
        entry_points=entry_points
    )


if __name__ == "__main__":
    setup_package()
