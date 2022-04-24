#!/usr/bin/env bash

set -e

rm -rf dist

python setup.py sdist

twine upload dist/*
