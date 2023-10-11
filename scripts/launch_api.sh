#!/bin/bash

echo "hello"

cd "$(dirname "$0")/.." || exit

# uvicorn app.main:app --reload
# python -m main