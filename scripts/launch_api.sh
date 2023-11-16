#!/bin/bash

# Environment variable to access private endpoints
export MY_API_KEY="my_api_key"

# Navigate to the correct directory and start the API
cd "$(dirname "$0")/.." || exit
python -m app.main