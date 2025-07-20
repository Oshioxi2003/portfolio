# Portfolio Website - Django

Portfolio website cá nhân với đầy đủ chức năng quản lý khóa học, blog, podcast và liên hệ.

## Tính năng

- 🏠 Trang Home với profile và thống kê
- 📚 Quản lý khóa học
- ✍️ Blog với bài viết truyền cảm hứng  
- 🎙️ Podcast/Media section
- 📩 Form liên hệ
- 🔧 Admin Dashboard quản lý toàn bộ

## Cài đặt

1. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

2. Migrate database:
```bash
python manage.py migrate
```

3. Tạo superuser:
```bash
python manage.py createsuperuser
```

4. Chạy server:
```bash
python manage.py runserver
```

## Cấu trúc Project

- `portfolio/` - Django app chính
- `templates/` - Templates HTML
- `static/` - CSS, JS, images
- `media/` - User uploaded files

## Công nghệ sử dụng

- Django 4.2
- Bootstrap 5
- SQLite database 