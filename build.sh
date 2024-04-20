#!/usr/bin/env bash
# Exit on error
set -o errexit

# Build the project
echo "Building the project..."
poetry install --no-dev

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Start the server
echo "Starting the server..."
uvicorn config.wsgi:application
