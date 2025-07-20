#!/bin/bash

# Exit on any error
set -e

echo "🚀 Starting PRODUCTION Django Portfolio Application..."

# Wait for MySQL to be ready
echo "⏳ Waiting for MySQL database..."
while ! nc -z $DB_HOST $DB_PORT; do
  echo "Waiting for MySQL at $DB_HOST:$DB_PORT..."
  sleep 3
done
echo "✅ MySQL is ready!"

# Run database migrations
echo "🔄 Running database migrations..."
python manage.py makemigrations --no-input
python manage.py migrate --no-input

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput --clear

# Create superuser if it doesn't exist
echo "👤 Checking superuser..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
import os
User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@oshioxi.site')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'Superuser {username} created successfully!')
else:
    print(f'Superuser {username} already exists!')
EOF

# Populate sample data (only if no data exists)
echo "📊 Checking sample data..."
python manage.py shell << EOF
from portfolio.models import Profile
if not Profile.objects.exists():
    from django.core.management import call_command
    try:
        call_command('populate_data')
        print('Sample data populated successfully!')
    except:
        print('Sample data command not found or failed')
else:
    print('Sample data already exists!')
EOF

echo "🎉 PRODUCTION Django application is ready!"
echo "🌐 Portfolio: https://oshioxi.site"
echo "📝 Admin panel: https://oshioxi.site/admin"

# Execute the main command
exec "$@" 