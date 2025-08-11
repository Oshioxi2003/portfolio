# 🚀 Portfolio Website - Django

Portfolio website hiện đại với mobile optimization, theme switching và multi-language support.

## ⚡ Quick Start

```bash
# Clone & Install
git clone <your-repo>
cd portfolio
pip install -r requirements.txt

# Setup Database
python manage.py migrate
python manage.py populate_data
python manage.py createsuperuser

# Run Server
python manage.py runserver
```

**URLs:**
- Portfolio: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## 🌟 Features

### 📱 Mobile-First Design
- **Bottom Navigation:** Touch-friendly navigation bar
- **Glassmorphism UI:** Modern blur effects
- **Responsive:** Works on all devices (≥44px touch targets)
- **Hover Expand:** Desktop icons expand with text labels

### 🎨 Theme & Language
- **Dark/Light Mode:** Instant theme switching
- **Vietnamese/English:** Real-time language toggle
- **Persistent Settings:** Saved in localStorage
- **Smooth Animations:** 60fps CSS transitions

### 📄 Content Management
- **Home:** Profile với featured content
- **Courses/Projects:** Filterable với pagination
- **Blog:** Search & tags system
- **Podcast:** Media player integration
- **Contact:** Functional contact form
- **Admin Dashboard:** Full content management

## 🚀 Deploy to Render (Free)

### Ready-to-Deploy Features:
- ✅ SQLite database (no external DB needed)
- ✅ Docker optimized for Render
- ✅ Auto-build scripts
- ✅ Environment templates

### Deploy Steps:
```bash
# 1. Push to GitHub
git push origin main

# 2. Create Render account at render.com
# 3. New → Blueprint → Connect repo
# 4. Deploy automatically!
```

**Cost:** FREE (750 hours/month + 1GB storage)

## 📱 Navigation System

### Desktop (>768px):
- Vertical navigation (right side)
- 50px icons with hover expansion
- Text labels slide in smoothly

### Mobile (≤768px):
- Bottom glassmorphism bar
- Horizontal layout, 45px icons
- Touch-optimized spacing

### Small Mobile (≤480px):
- 40px icons, reduced animations
- Optimized for battery life

## 🎨 Theme Controls

### Theme Switcher:
- **Location:** Top-right corner
- **Icons:** Sun/Moon
- **Toggle:** Click to switch instantly

### Language Switcher:
- **Location:** Next to theme switcher
- **Display:** EN/VI indicator
- **Scope:** All navigation & content

## 🛠️ Customization

### Update Content:
1. **Profile:** Admin → Profiles → Edit info
2. **Projects:** Admin → Courses → Add/Edit courses
3. **Blog:** Admin → Blog Posts → Write posts
4. **Podcast:** Admin → Podcast Episodes → Add episodes

### Styling:
- **CSS:** Edit `templates/portfolio/base.html`
- **Colors:** Update CSS variables
- **Layout:** Modify templates in `templates/portfolio/`

## 🔧 Tech Stack

**Backend:**
- Django 4.2 + SQLite
- REST API với Django REST Framework
- Gunicorn WSGI server

**Frontend:**
- Bootstrap 5 + Font Awesome
- CSS Variables cho theming
- JavaScript cho interactions
- Google Fonts (Inter)

**Deployment:**
- Render.com (free tier)
- Docker containerization
- Automatic HTTPS

## 📊 Project Structure

```
portfolio/
├── portfolio/              # Main app
│   ├── models.py           # Database models
│   ├── views.py            # Page views
│   ├── api_views.py        # REST API
│   └── admin.py            # Admin interface
├── templates/              # HTML templates
├── static/                 # CSS/JS assets
├── requirements.txt        # Dependencies
├── render.yaml            # Deployment config
└── build.sh               # Build script
```

## 🚨 Troubleshooting

### Common Issues:
```bash
# Migration errors
python manage.py migrate --check

# Static files not loading
python manage.py collectstatic

# Check Django setup
python manage.py check
```

### Render Deploy Issues:
- Check Python version: 3.11.9
- Verify environment variables
- Monitor build logs in dashboard

## 📞 Support

**Documentation:**
- [Render Docs](https://render.com/docs)
- [Django on Render](https://render.com/docs/deploy-django)

**Debug Commands:**
```bash
python manage.py check
python manage.py migrate --check
python manage.py collectstatic --dry-run
```

## ✅ Features Checklist

- [x] Mobile-responsive navigation
- [x] Dark/Light theme switching  
- [x] Vietnamese/English support
- [x] Admin content management
- [x] Contact form functionality
- [x] SEO-optimized structure
- [x] Ready for production deploy
- [x] Free hosting on Render

## 🎉 Result

**Professional portfolio với:**
- ⚡ Modern, mobile-first design
- 🌗 Theme & language switching
- 📱 Touch-optimized navigation
- 🔧 Full admin dashboard
- 🚀 One-click deploy to Render
- 💰 Completely free hosting

**Ready to showcase your skills! 🌟**

---

**Quick Commands:**
```bash
python manage.py runserver     # Development
python manage.py populate_data # Sample data
git push origin main          # Deploy to Render
```