# 🐳 Docker Setup Guide - Django Portfolio với MySQL

## 📋 **Yêu cầu hệ thống**

### **Software cần thiết:**
- ✅ **Docker Desktop** (Windows/Mac) hoặc **Docker Engine** (Linux)
- ✅ **Docker Compose** (thường đi kèm với Docker Desktop)
- ✅ **Git** (để clone repository)

### **Kiểm tra Docker:**
```bash
docker --version
docker-compose --version
```

## 🚀 **Quick Start**

### **1. Clone và Setup:**
```bash
# Clone repository
git clone <your-repo-url>
cd portfolio

# Copy environment file
cp env_template.txt .env

# Edit .env file với settings của bạn
# (Xem phần Environment Variables bên dưới)
```

### **2. Build và chạy:**
```bash
# Build và start tất cả services
docker-compose up --build

# Hoặc chạy background:
docker-compose up --build -d
```

### **3. Access ứng dụng:**
- **Website:** http://localhost
- **Django Direct:** http://localhost:8000  
- **Admin:** http://localhost:8000/admin
- **MySQL:** localhost:3306

**Credentials mặc định:**
- **Admin:** admin / admin123
- **MySQL Root:** root_password123

## 🏗️ **Architecture Overview**

### **Services Container:**

```
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│   Nginx Proxy   │  │  Django Web     │  │   MySQL DB      │
│   Port: 80/443  │◄─┤   Port: 8000    │◄─┤   Port: 3306    │
│                 │  │                 │  │                 │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

### **1. 🗄️ MySQL Database (db)**
- **Image:** mysql:8.0
- **Container:** portfolio_mysql
- **Port:** 3306
- **Volume:** mysql_data (persistent)

### **2. 🐍 Django Web (web)**
- **Build:** Custom Dockerfile
- **Container:** portfolio_web  
- **Port:** 8000
- **Volumes:** Code, static files, media files

### **3. 🌐 Nginx Proxy (nginx)**
- **Image:** nginx:alpine
- **Container:** portfolio_nginx
- **Ports:** 80, 443
- **Features:** Static files serving, reverse proxy

## ⚙️ **Environment Variables**

### **Tạo file .env:**
```bash
cp env_template.txt .env
```

### **Cấu hình cơ bản:**
```env
# Django Settings
DEBUG=True
SECRET_KEY=change-this-super-secret-key-in-production
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0,your-domain.com

# Database Settings  
DB_NAME=portfolio_db
DB_USER=portfolio_user
DB_PASSWORD=your_secure_password
DB_ROOT_PASSWORD=your_root_password
DB_HOST=db
DB_PORT=3306

# Email Settings (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## 🔧 **Detailed Commands**

### **Development:**
```bash
# Start services
docker-compose up

# Start in background
docker-compose up -d

# Build và start
docker-compose up --build

# View logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f web
docker-compose logs -f db
```

### **Database Commands:**
```bash
# Django migrations
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Populate sample data
docker-compose exec web python manage.py populate_data

# Django shell
docker-compose exec web python manage.py shell
```

### **Static Files:**
```bash
# Collect static files
docker-compose exec web python manage.py collectstatic --noinput

# Clear static files
docker-compose exec web rm -rf staticfiles/*
```

## 🗃️ **Data Management**

### **Backup Database:**
```bash
# Create backup
docker-compose exec db mysqldump -u root -p"$DB_ROOT_PASSWORD" portfolio_db > backup.sql

# Restore backup
docker-compose exec -T db mysql -u root -p"$DB_ROOT_PASSWORD" portfolio_db < backup.sql
```

### **Volume Management:**
```bash
# List volumes
docker volume ls

# Remove all volumes (⚠️ Mất dữ liệu!)
docker-compose down -v

# Backup volume
docker run --rm -v portfolio_mysql_data:/data -v $(pwd):/backup alpine tar czf /backup/mysql_backup.tar.gz /data
```

## 🐛 **Troubleshooting**

### **Common Issues:**

**1. Port đã sử dụng:**
```bash
# Check ports
netstat -tulpn | grep :80
netstat -tulpn | grep :3306

# Stop conflicting services
sudo systemctl stop apache2  # hoặc nginx
sudo systemctl stop mysql
```

**2. Permission denied:**
```bash
# Fix Docker permissions (Linux)
sudo usermod -aG docker $USER
newgrp docker

# Fix file permissions
sudo chown -R $USER:$USER .
```

**3. MySQL connection failed:**
```bash
# Check MySQL container
docker-compose logs db

# Test connection
docker-compose exec web python manage.py dbshell
```

**4. Static files không load:**
```bash
# Rebuild static files
docker-compose exec web python manage.py collectstatic --noinput --clear

# Check nginx config
docker-compose exec nginx nginx -t
```

### **Reset Everything:**
```bash
# Stop và remove containers
docker-compose down

# Remove volumes (⚠️ Mất dữ liệu!)
docker-compose down -v

# Remove images
docker-compose down --rmi all

# Clean rebuild
docker-compose up --build --force-recreate
```

## 🚀 **Production Deployment**

### **Environment Updates:**
```env
DEBUG=False
SECRET_KEY=super-secure-production-key
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
```

### **Security Enhancements:**
```bash
# Use specific image tags
# Update docker-compose.yml:
# mysql:8.0.35 thay vì mysql:8.0

# Enable SSL (nginx.conf)
# Thêm SSL certificates
# Configure firewall rules
```

### **Performance Tuning:**
```yaml
# docker-compose.yml updates
services:
  web:
    deploy:
      resources:
        limits:
          memory: 512M
        reservations:
          memory: 256M
  
  db:
    command: >
      --default-authentication-plugin=mysql_native_password
      --innodb-buffer-pool-size=256M
      --max-connections=100
```

## 📊 **Monitoring**

### **Health Checks:**
```bash
# Container status
docker-compose ps

# Resource usage
docker stats

# Health endpoints
curl http://localhost/health/
curl http://localhost:8000/admin/
```

### **Log Monitoring:**
```bash
# All logs
docker-compose logs -f

# Follow specific service
docker-compose logs -f --tail=100 web

# Save logs to file
docker-compose logs > app.log
```

## 📁 **File Structure**

```
portfolio/
├── 📄 docker-compose.yml       # Orchestration config
├── 📄 Dockerfile              # Django container build
├── 📄 nginx.conf               # Nginx configuration
├── 📄 docker-entrypoint.sh     # Startup script
├── 📄 requirements.txt         # Python dependencies
├── 📄 .env                     # Environment variables
├── 📄 .dockerignore           # Docker ignore patterns
├── 📁 portfolio_site/          # Django project
├── 📁 portfolio/               # Django app
├── 📁 templates/               # HTML templates
├── 📁 static/                  # Static source files
├── 📁 staticfiles/             # Collected static files
├── 📁 media/                   # User uploads
└── 📁 mysql-init/              # MySQL init scripts
```

## 🎯 **Features Included**

### **✅ Application Features:**
- Multi-container Docker setup
- MySQL 8.0 database
- Nginx reverse proxy
- Static files serving  
- Media files handling
- Auto-migrations on startup
- Sample data population
- Health checks
- Logging

### **✅ Security Features:**
- Environment variables
- Secret key management
- CORS configuration
- Security headers
- SSL-ready nginx config
- Database authentication

### **✅ Development Features:**
- Hot-reload (development)
- Volume mounting
- Log aggregation
- Database backups
- Easy reset/rebuild

## 🎉 **Success Verification**

### **After successful setup:**

1. **✅ Website accessible:** http://localhost
2. **✅ Admin panel:** http://localhost/admin (admin/admin123)
3. **✅ Database connected:** No errors in logs
4. **✅ Static files:** CSS/JS loading properly
5. **✅ Media files:** Image uploads working
6. **✅ Navigation:** Mobile/desktop responsive
7. **✅ Themes:** Dark/light mode switching
8. **✅ Languages:** Vietnamese/English toggle

### **Performance Check:**
```bash
# Container health
docker-compose ps

# Database connection
docker-compose exec web python manage.py check --database default

# Static files
curl -I http://localhost/static/css/style.css
```

## 📞 **Support**

### **Nếu gặp vấn đề:**
1. Check logs: `docker-compose logs -f`
2. Verify .env file có đầy đủ variables
3. Ensure ports 80, 3306, 8000 available
4. Try rebuild: `docker-compose up --build --force-recreate`

**🐳 Docker setup complete! Portfolio ready for development and production! 🚀** 