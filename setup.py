#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='hydra-debug',
    version='0.1',
    description='Hydra client that does nothing, for debug purposes', 
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'hydra-base',
        'hydra-client-python',
    ],
    entry_points='''
    [console_scripts]
    hydra-debug=hydra_debug.cli:start_cli
    ''',
)
