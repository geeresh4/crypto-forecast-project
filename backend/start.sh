#!/bin/bash
# Start script for Render deployment

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}

