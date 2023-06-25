#!/bin/bash

set -e

poetry install
poetry run python ./src/main.py