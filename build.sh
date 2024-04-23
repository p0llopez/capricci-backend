#!/usr/bin/env bash
# Exit on error
set -o errexit

# Build the project
echo "Building the project..."
poetry install --no-dev --no-root

# Convert static asset files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create Superuser if needed
echo "Creating superuser..."
if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input
fi
