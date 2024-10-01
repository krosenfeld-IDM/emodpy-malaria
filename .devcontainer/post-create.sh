#!/bin/bash

pip install -r requirements.txt --index-url=https://packages.idmod.org/api/pypi/pypi-production/simple
cd docs
pip install -r requirements.txt --index-url=https://packages.idmod.org/api/pypi/pypi-production/simple
cd ..
pip install -e . --index-url=https://packages.idmod.org/api/pypi/pypi-production/simple