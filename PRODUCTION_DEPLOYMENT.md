# 🚀 Production Deployment Guide - oshioxi.site

## 🛠️ **Pre-Deployment Steps**

### **1. Fix Disk Space Issue:**
```bash
# Start Docker Desktop first!
# Then clean up Docker:
docker system prune -a --volumes
docker builder prune -a

# Clean Windows temp files:
cleanmgr.exe

# Check available space:
dir C:\ | findstr "bytes free"
```

### **2. Domain Setup:**
- ✅ **Domain:** oshioxi.site
- ✅ **DNS A Record:** Point to your server IP
- ✅ **WWW CNAME:** Point www.oshioxi.site to oshioxi.site

## 📦 **Optimized Setup**

### **✅ Requirements Fixed:**
```txt
Django==4.2.7
mysqlclient==2.2.0
Pillow==10.1.0
python-decouple==3.8
django-environ==0.11.2
gunicorn==21.2.0
whitenoise==6.6.0
django-cors-headers==4.3.1
requests==2.31.0
```
**Reduced from 31 packages to 9 packages** - Saves ~2GB disk space!

## 🌐 **Server Setup**

### **1. Server Requirements:**
- **OS:** Ubuntu 20.04+ / CentOS 8+ / Debian 11+
- **RAM:** Minimum 2GB (Recommended 4GB)
- **Storage:** Minimum 10GB free space
- **CPU:** 1 vCPU minimum (2+ recommended)

### **2. Install Docker on Server:**
```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
sudo systemctl enable docker
sudo systemctl start docker

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.21.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## 🔧 **Deployment Process**

### **1. Clone Repository:**
```bash
# On your server
git clone <your-repo-url> oshioxi-portfolio
cd oshioxi-portfolio
```

### **2. Environment Configuration:**
```bash
# Copy production environment template
cp production_env_template.txt .env

# Edit with your secure values
nano .env
```

### **📝 Critical Environment Variables:**
```env
# MUST CHANGE THESE:
SECRET_KEY=generate-a-50-character-random-secret-key
DB_PASSWORD=create-secure-db-password
DB_ROOT_PASSWORD=create-secure-root-password
DJANGO_SUPERUSER_PASSWORD=create-admin-password

# Email (optional)
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### **3. Generate Secret Key:**
```python
# Run this to generate secure secret key:
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### **4. Deploy with Docker:**
```bash
# Build and start production services
docker-compose -f docker-compose.prod.yml up --build -d

# Check status
docker-compose -f docker-compose.prod.yml ps

# View logs
docker-compose -f docker-compose.prod.yml logs -f
```

## 🔒 **SSL Certificate Setup**

### **1. Initial SSL Certificate:**
```bash
# Get initial certificate
docker-compose -f docker-compose.prod.yml run --rm certbot certonly --webroot --webroot-path=/var/www/certbot --email your-email@example.com --agree-tos --no-eff-email -d oshioxi.site -d www.oshioxi.site

# Restart nginx with SSL
docker-compose -f docker-compose.prod.yml restart nginx
```

### **2. Auto-Renewal Setup:**
```bash
# Add to crontab for auto-renewal
sudo crontab -e

# Add this line:
0 3 * * * cd /path/to/oshioxi-portfolio && docker-compose -f docker-compose.prod.yml run --rm certbot renew && docker-compose -f docker-compose.prod.yml restart nginx
```

## 🎯 **Production Architecture**

```
Internet → Nginx (Port 80/443) → Django (Port 8000) → MySQL (Port 3306)
            ↓
        SSL Termination
        Static Files
        Rate Limiting
        Security Headers
```

### **🏗️ Services:**
- **🌐 Nginx:** Reverse proxy, SSL, static files, security
- **🐍 Django:** Web application with Gunicorn
- **🗄️ MySQL:** Database with persistent storage
- **🔒 Certbot:** SSL certificate management

## 📊 **Monitoring & Health**

### **1. Health Checks:**
```bash
# Container status
docker-compose -f docker-compose.prod.yml ps

# Application health
curl https://oshioxi.site/health/

# SSL certificate status
echo | openssl s_client -servername oshioxi.site -connect oshioxi.site:443 2>/dev/null | openssl x509 -noout -dates
```

### **2. Log Monitoring:**
```bash
# All services logs
docker-compose -f docker-compose.prod.yml logs -f

# Specific service
docker-compose -f docker-compose.prod.yml logs -f web
docker-compose -f docker-compose.prod.yml logs -f nginx

# Save logs to file
docker-compose -f docker-compose.prod.yml logs > production.log
```

### **3. Resource Monitoring:**
```bash
# Container resources
docker stats

# System resources
htop
df -h
free -h
```

## 🔐 **Security Features**

### **✅ Implemented Security:**
- **HTTPS Enforced:** All HTTP redirects to HTTPS
- **Security Headers:** XSS, CSRF, Content-Type protection
- **Rate Limiting:** API and admin login protection
- **HSTS:** Strict Transport Security
- **CSP:** Content Security Policy
- **Non-root User:** Django runs as non-root
- **Secure Passwords:** Environment variable protection

### **🛡️ Additional Security Steps:**
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Configure firewall
sudo ufw enable
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Disable SSH root login
sudo nano /etc/ssh/sshd_config
# Set: PermitRootLogin no
sudo systemctl restart ssh
```

## 🗂️ **Database Management**

### **1. Backup Database:**
```bash
# Create backup
docker-compose -f docker-compose.prod.yml exec db mysqldump -u root -p"$DB_ROOT_PASSWORD" oshioxi_portfolio > backup_$(date +%Y%m%d_%H%M%S).sql

# Schedule daily backups
sudo crontab -e
# Add: 0 2 * * * cd /path/to/oshioxi-portfolio && docker-compose -f docker-compose.prod.yml exec db mysqldump -u root -p"password" oshioxi_portfolio > /backups/backup_$(date +\%Y\%m\%d).sql
```

### **2. Restore Database:**
```bash
# Restore from backup
docker-compose -f docker-compose.prod.yml exec -T db mysql -u root -p"$DB_ROOT_PASSWORD" oshioxi_portfolio < backup_file.sql
```

## 🔄 **Updates & Maintenance**

### **1. Application Updates:**
```bash
# Pull latest code
git pull origin main

# Rebuild and restart
docker-compose -f docker-compose.prod.yml up --build -d

# Run migrations if needed
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
```

### **2. System Maintenance:**
```bash
# Clean old Docker images
docker system prune -a

# Update Docker images
docker-compose -f docker-compose.prod.yml pull
docker-compose -f docker-compose.prod.yml up -d
```

## 🚨 **Troubleshooting**

### **Common Issues:**

**1. SSL Certificate Failed:**
```bash
# Check nginx config
docker-compose -f docker-compose.prod.yml exec nginx nginx -t

# Verify domain points to server
nslookup oshioxi.site

# Check port 80 accessibility
curl -I http://oshioxi.site/.well-known/acme-challenge/test
```

**2. Database Connection Error:**
```bash
# Check MySQL container
docker-compose -f docker-compose.prod.yml logs db

# Test database connection
docker-compose -f docker-compose.prod.yml exec web python manage.py dbshell
```

**3. Static Files Not Loading:**
```bash
# Collect static files
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput --clear

# Check nginx config
docker-compose -f docker-compose.prod.yml exec nginx nginx -t
```

## 📍 **Access Points**

### **🌐 Production URLs:**
- **Website:** https://oshioxi.site
- **Admin Panel:** https://oshioxi.site/admin
- **Health Check:** https://oshioxi.site/health/

### **🔑 Default Credentials:**
- **Admin:** admin / [from DJANGO_SUPERUSER_PASSWORD]
- **Database:** oshioxi_user / [from DB_PASSWORD]

## 📈 **Performance Optimization**

### **1. Database Optimization:**
```sql
-- MySQL performance tuning (run in MySQL shell)
SET GLOBAL innodb_buffer_pool_size = 256M;
SET GLOBAL max_connections = 100;
```

### **2. Django Optimization:**
```python
# In settings.py production:
CONN_MAX_AGE = 60
DATABASES['default']['CONN_MAX_AGE'] = 60
```

### **3. Nginx Caching:**
```nginx
# Add to nginx.prod.conf if needed:
location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

## 🎉 **Success Checklist**

### **✅ Deployment Verification:**
1. **Domain accessible:** https://oshioxi.site ✅
2. **SSL certificate valid:** Green lock in browser ✅
3. **Admin panel works:** https://oshioxi.site/admin ✅
4. **Mobile navigation:** Responsive design works ✅
5. **Theme switching:** Dark/light mode works ✅
6. **Language switching:** Vietnamese/English works ✅
7. **Contact form:** Email sending works ✅
8. **Media uploads:** Images upload via admin ✅

### **🔍 Performance Check:**
```bash
# Website speed test
curl -w "@curl-format.txt" -o /dev/null -s https://oshioxi.site

# SSL rating
curl -s "https://api.ssllabs.com/api/v3/analyze?host=oshioxi.site"
```

## 📞 **Support & Maintenance**

### **🛠️ Regular Tasks:**
- **Daily:** Check logs and health status
- **Weekly:** Review security updates
- **Monthly:** Database backup verification
- **Quarterly:** SSL certificate renewal check

### **📧 Emergency Contacts:**
- **Server Issues:** Check hosting provider dashboard
- **Domain Issues:** Check domain registrar
- **SSL Issues:** Let's Encrypt status page

**🎊 oshioxi.site portfolio is ready for production! 🚀**

---

## 💡 **Quick Commands Reference**

```bash
# Start production
docker-compose -f docker-compose.prod.yml up -d

# View logs
docker-compose -f docker-compose.prod.yml logs -f

# Restart services
docker-compose -f docker-compose.prod.yml restart

# Stop everything
docker-compose -f docker-compose.prod.yml down

# Update application
git pull && docker-compose -f docker-compose.prod.yml up --build -d
``` 