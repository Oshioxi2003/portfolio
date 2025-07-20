#!/usr/bin/env bash
# Render Build Script

set -o errexit  # exit on error

echo "🚀 Starting Render build process..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip==24.0 setuptools==69.5.1 wheel==0.42.0
pip install --no-cache-dir -c constraints.txt -r requirements.txt

# Set database path to persistent disk
export DB_PATH="/app/data/db.sqlite3"

# Create data directory if it doesn't exist
mkdir -p /app/data

# Collect static files
echo "📂 Collecting static files..."
python manage.py collectstatic --noinput --clear

# Run database migrations
echo "🗄️ Running database migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Create superuser if it doesn't exist
echo "👤 Creating superuser..."
python manage.py shell << EOF
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@oshioxi.site')  
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'✅ Superuser {username} created successfully!')
else:
    print(f'ℹ️ Superuser {username} already exists!')
EOF

# Populate sample data if needed
echo "📊 Checking sample data..."
python manage.py shell << EOF
from portfolio.models import Profile
if not Profile.objects.exists():
    print('📝 Creating sample data...')
    # Create basic profile
    profile = Profile.objects.create(
        name='Your Name',
        title='Web Developer',
        bio='Welcome to my portfolio website!',
        email='your.email@example.com',
        location='Vietnam'
    )
    print(f'✅ Sample profile created: {profile.name}')
else:
    print('ℹ️ Sample data already exists!')
EOF

echo "🎉 Build completed successfully!" 