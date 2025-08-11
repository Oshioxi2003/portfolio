# Hướng dẫn triển khai Django Portfolio lên Heroku

## ⚠️ Lưu ý quan trọng về Dependencies

**Vấn đề đã fix:**
- ✅ Slug size quá lớn (3GB -> ~50MB)  
- ✅ Runtime.txt deprecated
- ✅ Loại bỏ PyTorch, OpenAI Whisper và các ML libraries không cần thiết

## 1. Cài đặt Heroku CLI

Tải và cài đặt Heroku CLI từ: https://devcenter.heroku.com/articles/heroku-cli

## 2. Đăng nhập Heroku

```bash
heroku login
```

## 3. Tạo ứng dụng Heroku

```bash
heroku create your-app-name
```

## 4. Cấu hình biến môi trường trên Heroku

```bash
# Django Settings
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"

# Security
heroku config:set CSRF_TRUSTED_ORIGINS="https://your-app-name.herokuapp.com"

# Email (Tùy chọn)
heroku config:set EMAIL_HOST="smtp.gmail.com"
heroku config:set EMAIL_PORT=587
heroku config:set EMAIL_USE_TLS=True
heroku config:set EMAIL_HOST_USER="your-email@gmail.com"
heroku config:set EMAIL_HOST_PASSWORD="your-app-password"
```

## 5. Thêm PostgreSQL Database

```bash
heroku addons:create heroku-postgresql:essential-0
```

## 6. Deploy ứng dụng

```bash
git add .
git commit -m "Configure for Heroku deployment"
git push heroku main
```

## 7. Chạy migrations

```bash
heroku run python manage.py migrate
```

## 8. Tạo superuser (Tùy chọn)

```bash
heroku run python manage.py createsuperuser
```

## 9. Collect static files (Nếu cần)

```bash
heroku run python manage.py collectstatic --noinput
```

## 10. Xem logs nếu có lỗi

```bash
heroku logs --tail
```

## Ghi chú quan trọng:

1. **SECRET_KEY**: Tạo một SECRET_KEY mới bằng cách chạy:
   ```python
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **Database**: Heroku sẽ tự động tạo biến DATABASE_URL cho PostgreSQL

3. **Static Files**: WhiteNoise đã được cấu hình để serve static files

4. **Media Files**: Để upload files, bạn cần cấu hình AWS S3 hoặc Cloudinary

5. **CORS**: Cập nhật CORS_ALLOWED_ORIGINS trong settings.py nếu cần

6. **Dependencies đã tối ưu**: 
   - Loại bỏ PyTorch (865MB) và OpenAI Whisper
   - Loại bỏ các ML libraries không cần thiết
   - Slug size giảm từ 3GB xuống ~50MB

7. **Python Version**: Sử dụng `.python-version` thay vì `runtime.txt`

## Troubleshooting:

- Nếu có lỗi build: kiểm tra requirements.txt
- Nếu có lỗi database: chạy `heroku run python manage.py migrate`
- Nếu có lỗi static files: chạy `heroku run python manage.py collectstatic`
