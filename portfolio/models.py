from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import os
from datetime import datetime


def profile_avatar_path(instance, filename):
    """Generate upload path for profile avatars"""
    ext = filename.split('.')[-1]
    filename = f"avatar_{instance.name.replace(' ', '_').lower()}.{ext}"
    return os.path.join('profile', 'avatars', filename)


def course_thumbnail_path(instance, filename):
    """Generate upload path for course thumbnails"""
    ext = filename.split('.')[-1]
    filename = f"{instance.slug}.{ext}"
    return os.path.join('courses', 'thumbnails', filename)


def blog_image_path(instance, filename):
    """Generate upload path for blog images"""
    ext = filename.split('.')[-1]
    year = datetime.now().year
    month = datetime.now().month
    filename = f"{instance.slug}.{ext}"
    return os.path.join('blog', str(year), f"{month:02d}", filename)


def podcast_thumbnail_path(instance, filename):
    """Generate upload path for podcast thumbnails"""
    ext = filename.split('.')[-1]
    season = instance.season
    episode = instance.episode_number
    filename = f"s{season}e{episode:02d}.{ext}"
    return os.path.join('podcast', f'season_{season}', filename)


class Profile(models.Model):
    """Model lưu thông tin profile cá nhân"""
    name = models.CharField("Tên", max_length=100)
    tagline = models.CharField("Tagline", max_length=200)
    bio = models.TextField("Mô tả bản thân")
    avatar = models.ImageField("Ảnh đại diện", upload_to=profile_avatar_path, blank=True)
    email = models.EmailField("Email")
    phone = models.CharField("Số điện thoại", max_length=20, blank=True)
    
    # Social links
    facebook_url = models.URLField("Facebook", blank=True)
    instagram_url = models.URLField("Instagram", blank=True)
    youtube_url = models.URLField("YouTube", blank=True)
    linkedin_url = models.URLField("LinkedIn", blank=True)
    
    # Statistics
    total_students = models.PositiveIntegerField("Tổng học viên", default=0)
    total_views = models.PositiveIntegerField("Tổng lượt xem", default=0)
    years_experience = models.PositiveIntegerField("Năm kinh nghiệm", default=0)
    courses_created = models.PositiveIntegerField("Khóa học đã tạo", default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
    
    def __str__(self):
        return self.name


class Course(models.Model):
    """Model cho khóa học"""
    title = models.CharField("Tiêu đề", max_length=200)
    slug = models.SlugField("Slug", unique=True, blank=True)
    description = models.TextField("Mô tả")
    thumbnail = models.ImageField("Ảnh thumbnail", upload_to=course_thumbnail_path, blank=True)
    icon = models.CharField("Icon class (Bootstrap/Font Awesome)", max_length=100, blank=True)
    
    # Course details
    duration = models.CharField("Thời lượng", max_length=50, blank=True)
    level = models.CharField("Cấp độ", max_length=50, 
                           choices=[
                               ('beginner', 'Người mới bắt đầu'),
                               ('intermediate', 'Trung cấp'),
                               ('advanced', 'Nâng cao')
                           ], default='beginner')
    price = models.DecimalField("Giá", max_digits=10, decimal_places=2, default=0)
    
    # External links
    course_url = models.URLField("Link khóa học", blank=True)
    enrollment_required = models.BooleanField("Yêu cầu đăng ký", default=True)
    
    # Status
    is_active = models.BooleanField("Đang hoạt động", default=True)
    featured = models.BooleanField("Nổi bật", default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Khóa học"
        verbose_name_plural = "Khóa học"
        ordering = ['-featured', '-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title


class BlogPost(models.Model):
    """Model cho bài viết blog"""
    title = models.CharField("Tiêu đề", max_length=200)
    slug = models.SlugField("Slug", unique=True, blank=True)
    content = models.TextField("Nội dung")
    excerpt = models.TextField("Tóm tắt", max_length=300, blank=True)
    featured_image = models.ImageField("Ảnh đại diện", upload_to=blog_image_path, blank=True)
    
    # Meta
    tags = models.CharField("Tags (phân cách bằng dấu phẩy)", max_length=200, blank=True)
    read_time = models.PositiveIntegerField("Thời gian đọc (phút)", default=5)
    
    # Status
    is_published = models.BooleanField("Đã xuất bản", default=True)
    featured = models.BooleanField("Nổi bật", default=False)
    
    published_date = models.DateTimeField("Ngày xuất bản", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Bài viết"
        verbose_name_plural = "Bài viết"
        ordering = ['-published_date']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.excerpt and self.content:
            # Tạo excerpt từ 50 từ đầu của content
            words = self.content.split()[:50]
            self.excerpt = ' '.join(words) + '...'
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})
    
    def get_tags_list(self):
        """Trả về list tags"""
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
    
    def __str__(self):
        return self.title


class PodcastEpisode(models.Model):
    """Model cho podcast episode"""
    title = models.CharField("Tiêu đề", max_length=200)
    slug = models.SlugField("Slug", unique=True, blank=True)
    description = models.TextField("Mô tả")
    thumbnail = models.ImageField("Ảnh thumbnail", upload_to=podcast_thumbnail_path, blank=True)
    
    # Media
    audio_url = models.URLField("Link audio", blank=True)
    video_embed_url = models.TextField("Embed code video", blank=True)
    duration = models.CharField("Thời lượng", max_length=20, blank=True)
    
    # Episode info
    episode_number = models.PositiveIntegerField("Số tập", unique=True)
    season = models.PositiveIntegerField("Mùa", default=1)
    
    # External links
    spotify_url = models.URLField("Spotify", blank=True)
    apple_url = models.URLField("Apple Podcast", blank=True)
    youtube_url = models.URLField("YouTube", blank=True)
    
    # Status
    is_published = models.BooleanField("Đã xuất bản", default=True)
    featured = models.BooleanField("Nổi bật", default=False)
    
    published_date = models.DateTimeField("Ngày xuất bản", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Podcast Episode"
        verbose_name_plural = "Podcast Episodes"
        ordering = ['-episode_number']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('podcast_detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return f"Tập {self.episode_number}: {self.title}"


class ContactMessage(models.Model):
    """Model cho tin nhắn liên hệ"""
    name = models.CharField("Tên", max_length=100)
    email = models.EmailField("Email")
    subject = models.CharField("Chủ đề", max_length=200, blank=True)
    message = models.TextField("Nội dung")
    
    # Status
    is_read = models.BooleanField("Đã đọc", default=False)
    is_replied = models.BooleanField("Đã trả lời", default=False)
    
    created_at = models.DateTimeField("Ngày gửi", auto_now_add=True)
    
    class Meta:
        verbose_name = "Tin nhắn liên hệ"
        verbose_name_plural = "Tin nhắn liên hệ"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject or 'Liên hệ'}"
