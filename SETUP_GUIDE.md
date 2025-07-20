# Hướng dẫn Setup Portfolio Website

## 🎉 Chúc mừng! Website Portfolio đã được tạo thành công!

### ✅ Những gì đã hoàn thành:

1. **🏠 Trang Home** - Giới thiệu profile với thống kê và featured content
2. **📚 Trang Courses** - Danh sách khóa học với filter và pagination  
3. **✍️ Trang Blog** - Bài viết truyền cảm hứng với search và tags
4. **🎙️ Trang Podcast** - Episodes podcast với media links
5. **📩 Trang Contact** - Form liên hệ đầy đủ chức năng
6. **🔧 Admin Dashboard** - Quản lý toàn bộ nội dung
7. **🎨 Giao diện Bootstrap 5** - Responsive và modern

### 🚀 Cách chạy website:

1. **Cài đặt dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Chạy migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Tạo dữ liệu mẫu:**
   ```bash
   python manage.py populate_data
   ```

4. **Chạy server:**
   ```bash
   python manage.py runserver
   ```

5. **Truy cập website:** http://127.0.0.1:8000/

### 🔑 Truy cập Admin:

1. **Tạo superuser mới:**
   ```bash
   python manage.py createsuperuser
   ```

2. **Truy cập admin:** http://127.0.0.1:8000/admin/

3. **Quản lý nội dung:**
   - Profile: Thông tin cá nhân và thống kê
   - Courses: Danh sách khóa học
   - Blog Posts: Bài viết blog
   - Podcast Episodes: Tập podcast
   - Contact Messages: Tin nhắn liên hệ

### 📝 Cách tùy chỉnh:

1. **Cập nhật Profile:**
   - Vào Admin → Profiles → Sửa thông tin cá nhân
   - Upload avatar, cập nhật social links, thống kê

2. **Thêm khóa học:**
   - Admin → Courses → Add Course
   - Đánh dấu "Featured" để hiển thị trên Home

3. **Viết blog:**
   - Admin → Blog Posts → Add Blog Post
   - Sử dụng tags để phân loại bài viết

4. **Thêm podcast:**
   - Admin → Podcast Episodes → Add Episode
   - Embed video YouTube hoặc link audio

### 🎨 Tùy chỉnh giao diện:

- **CSS:** Sửa file `templates/portfolio/base.html` phần `<style>`
- **Logo:** Thay đổi navbar brand trong base template
- **Colors:** Cập nhật CSS variables và gradient colors
- **Layout:** Sửa templates trong `templates/portfolio/`

### 📱 Responsive Design:

Website đã được tối ưu cho:
- 📱 Mobile phones
- 📱 Tablets  
- 💻 Desktop
- 🖥️ Large screens

### 🔧 Features:

- ✅ SEO-friendly URLs với slugs
- ✅ Search và filter functionality
- ✅ Pagination cho danh sách
- ✅ Admin interface hoàn chỉnh
- ✅ Contact form validation
- ✅ Social media integration
- ✅ Modern UI/UX với Bootstrap 5
- ✅ Font Awesome icons
- ✅ Google Fonts (Inter)

### 🚀 Deploy Production:

1. **Cấu hình settings cho production**
2. **Setup static files serving**
3. **Configure database (PostgreSQL)**
4. **Setup domain và SSL**
5. **Configure email backend cho contact form**

### 📞 Hỗ trợ:

Nếu có vấn đề gì, hãy check:
1. Django server đang chạy: `python manage.py runserver`
2. Database đã migrate: `python manage.py migrate`
3. Dữ liệu mẫu đã tạo: `python manage.py populate_data`
4. Static files: Tạo thư mục `static/` nếu chưa có

---

**🎉 Chúc bạn thành công với website portfolio mới!** 