#!/usr/bin/env bash
# exit on error
set -o errexit

# Install setuptools first to handle pkg_resources dependencies
pip install setuptools
pip install -r requirements.txt

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --no-input

# Seed database with initial products if it's empty
python manage.py shell -c "from store.models import Product; import os; os.system('python seed_final_v7.py') if Product.objects.count() == 0 else print('Database already seeded')"
