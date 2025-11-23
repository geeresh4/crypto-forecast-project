#!/bin/bash
# Build script for Render
# This ensures Python 3.11 is used if available

# Try to use Python 3.11 if available
if command -v python3.11 &> /dev/null; then
    python3.11 -m pip install --upgrade pip
    python3.11 -m pip install -r requirements.txt
else
    # Fallback to default python
    pip install --upgrade pip
    pip install -r requirements.txt
fi

