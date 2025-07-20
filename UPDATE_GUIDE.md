# Cập Nhật Portfolio Website - Đào Huy Toàn

## 🎯 Thay Đổi Đã Thực Hiện

### ✅ **1. Cập Nhật Đường Dẫn Lưu Ảnh**

**Upload Paths được tổ chức theo cấu trúc:**
- **Profile avatars:** `profile/avatars/avatar_dao_huy_toan.jpg`
- **Course thumbnails:** `courses/thumbnails/{slug}.jpg`
- **Blog images:** `blog/{year}/{month:02d}/{slug}.jpg`
- **Podcast thumbnails:** `podcast/season_{season}/s{season}e{episode}.jpg`

**Functions đã thêm trong `portfolio/models.py`:**
```python
def profile_avatar_path(instance, filename)
def course_thumbnail_path(instance, filename)
def blog_image_path(instance, filename)
def podcast_thumbnail_path(instance, filename)
```

### ✅ **2. Placeholder Images từ placehold.co**

**Thay thế tất cả placeholder cũ với images từ placehold.co:**
- **Profile:** `https://placehold.co/300x350/1e1e1e/ffb400?text=PORTFOLIO`
- **Projects:** `https://placehold.co/600x300/1e1e1e/ffb400?text=PROJECT`
- **Blog posts:** `https://placehold.co/400x200/1e1e1e/ffb400?text=BLOG`
- **Podcast:** `https://placehold.co/400x200/1e1e1e/ffb400?text=PODCAST`
- **Detail pages:** `https://placehold.co/800x400/1e1e1e/ffb400?text={TYPE}`

**Color scheme:** Dark secondary (#1e1e1e) với primary yellow (#ffb400)

### ✅ **3. Cập Nhật Dữ Liệu Cho Đào Huy Toàn**

**Profile Information:**
- **Name:** Đào Huy Toàn
- **Email:** duct1531@gmail.com
- **Phone:** 0356581703
- **Tagline:** Web Developer & Technology Enthusiast
- **Bio:** Updated với English content về passion for web development
- **Social Links:** Updated với daohuytoann handles

**Projects Updated:**
1. E-Commerce Website (React.js, Node.js, MongoDB)
2. Portfolio Website (React, Tailwind CSS)
3. Task Management App (Real-time updates)
4. Weather Dashboard (Geolocation, 7-day forecast)
5. Blog Platform (Django, Bootstrap)

**Blog Posts in English:**
1. My Journey Into Web Development
2. Why I Choose React for Frontend Development
3. Best Practices for Clean Code

**Podcast Episodes:**
1. Getting Started in Web Development
2. Frontend vs Backend: What to Choose?
3. Building Your Developer Portfolio

## 🚀 **Cách Chạy Sau Khi Cập Nhật**

```bash
# 1. Apply migrations mới
python manage.py migrate

# 2. Cập nhật dữ liệu
python manage.py populate_data

# 3. Chạy server
python manage.py runserver
```

## 📂 **Cấu Trúc Media Files**

```
media/
├── profile/
│   └── avatars/
│       └── avatar_dao_huy_toan.jpg
├── courses/
│   └── thumbnails/
│       ├── e-commerce-website.jpg
│       ├── portfolio-website.jpg
│       └── ...
├── blog/
│   ├── 2024/
│   │   └── 01/
│   │       ├── my-journey-into-web-development.jpg
│   │       └── ...
└── podcast/
    ├── season_1/
    │   ├── s1e01.jpg
    │   ├── s1e02.jpg
    │   └── s1e03.jpg
```

## 🔧 **Admin Panel**

**Truy cập:** http://127.0.0.1:8000/admin/

**Quản lý:**
- Profile của Đào Huy Toàn
- Projects với GitHub links
- Blog posts in English
- Podcast episodes
- Contact messages

## 🎨 **Placeholder Images**

Tất cả placeholder images sử dụng placehold.co với:
- **Background:** #1e1e1e (dark secondary)
- **Text color:** #ffb400 (primary yellow)
- **Responsive sizes** cho different contexts

## 📱 **Features**

- ✅ Organized file upload paths
- ✅ Professional placeholder images
- ✅ Updated personal information
- ✅ English content for international appeal
- ✅ GitHub project links
- ✅ Modern tech stack showcase
- ✅ Responsive design maintained
- ✅ Dark theme với yellow accents

## 🔄 **Future Updates**

**Để thêm ảnh thật:**
1. Upload qua Django admin
2. Files sẽ được lưu theo organized paths
3. Placeholder images sẽ được thay thế tự động

**Để cập nhật projects:**
1. Vào Admin → Courses → Add/Edit
2. Thêm GitHub links và descriptions
3. Upload thumbnails nếu có

**Để thêm blog posts:**
1. Admin → Blog Posts → Add
2. Viết content in English
3. Add relevant tags

---

**🎉 Website hoàn toàn ready với identity mới của Đào Huy Toàn!** 