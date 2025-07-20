#!/bin/bash

# Exit on any error
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🐳 Starting Django Portfolio Application...${NC}"

# Wait for MySQL to be ready
echo -e "${YELLOW}⏳ Waiting for MySQL database...${NC}"
while ! nc -z $DB_HOST $DB_PORT; do
  echo "Waiting for MySQL at $DB_HOST:$DB_PORT..."
  sleep 2
done
echo -e "${GREEN}✅ MySQL is ready!${NC}"

# Run database migrations
echo -e "${YELLOW}🔄 Running database migrations...${NC}"
python manage.py makemigrations
python manage.py migrate

# Create superuser if it doesn't exist
echo -e "${YELLOW}👤 Creating superuser...${NC}"
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created successfully!')
else:
    print('Superuser already exists!')
EOF

# Collect static files
echo -e "${YELLOW}📦 Collecting static files...${NC}"
python manage.py collectstatic --noinput

# Populate sample data
echo -e "${YELLOW}📊 Populating sample data...${NC}"
python manage.py populate_data || echo "Sample data already exists or command not found"

echo -e "${GREEN}🚀 Django application is ready!${NC}"
echo -e "${GREEN}📝 Admin panel: http://localhost:8000/admin${NC}"
echo -e "${GREEN}🔑 Admin credentials: admin / admin123${NC}"

# Execute the main command
exec "$@" 