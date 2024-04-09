#!/bin/bash
set -e

# Check if a volume is mounted at /code
if [ ! -d "/code" ]; then
    echo "Error: Mount your code directory to /code in the container."
    exit 1
fi

# Navigate to the mounted code directory
cd /code

# Run safety to check for vulnerabilities in the mounted code
safety check --full-report
