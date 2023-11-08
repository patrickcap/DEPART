#!/bin/bash

set -e

cd "$(dirname "$0")/.." || exit

if ! mypy --install-types --non-interactive --config-file mypy.ini ./app ./test_api.py; then
    exit 1
fi
