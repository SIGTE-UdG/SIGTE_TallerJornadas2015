#!/bin/bash

BASE_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

sphinx-autobuild -b html $BASE_DIR $BASE_DIR/_build/html

