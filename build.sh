#!/usr/bin/env bash
# Exit on error
set -o errexit

# Build the project
echo "Building the project..."
poetry install --no-dev --no-root

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
