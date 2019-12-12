#!/bin/bash
pip install pipenv
# Install all the dependencies 
pipenv install --system --deploy --verbose 

# Clean up the cache
rm -rf ~/.cache/pip


