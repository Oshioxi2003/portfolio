import os
from datetime import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def profile_avatar_path(instance, filename):
    """Generate upload path for profile avatars."""
    ext = filename.split('.')[-1]
    filename = f"avatar_{instance.name.replace(' ', '_').lower()}.{ext}"
    return os.path.join('profile', 'avatars', filename)


def course_thumbnail_path(instance, filename):
    """Generate upload path for course thumbnails."""
    ext = filename.split('.')[-1]
    filename = f"{instance.slug}.{ext}"
    return os.path.join('courses', 'thumbnails', filename)


def blog_image_path(instance, filename):
    """Generate upload path for blog images."""
    ext = filename.split('.')[-1]
    year = datetime.now().year
    month = datetime.now().month
    filename = f"{instance.slug}.{ext}"
    return os.path.join('blog', str(year), f"{month:02d}", filename)


def podcast_thumbnail_path(instance, filename):
    """Generate upload path for podcast thumbnails."""
    ext = filename.split('.')[-1]
    season = instance.season
    episode = instance.episode_number
    filename = f"s{season}e{episode:02d}.{ext}"
    return os.path.join('podcast', f'season_{season}', filename)


class Profile(models.Model):
    """Model lưu thông tin profile cá nhân."""
    name = models.CharField("Tên", max_length=100)
    tagline = models.CharField("Tagline", max_length=200)
    bio = models.TextField("Mô tả bản thân")
    avatar = models.URLField("Link ảnh đại diện", blank=True, help_text="Link đến ảnh đại diện (VD: https://images.unsplash.com/...)")
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


class Category(models.Model):
    """Model cho categories của projects."""
    name = models.CharField("Tên category", max_length=100, unique=True)
    slug = models.SlugField("Slug", unique=True, blank=True)
    description = models.TextField("Mô tả", blank=True)
    icon = models.CharField("Icon class (Bootstrap/Font Awesome)", max_length=100, blank=True)
    color = models.CharField("Màu sắc (hex)", max_length=7, default="#007bff", help_text="VD: #007bff")
    
    is_active = models.BooleanField("Đang hoạt động", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Course(models.Model):
    """Model cho projects (trước đây là khóa học)."""
    title = models.CharField("Tiêu đề", max_length=200)
    slug = models.SlugField("Slug", unique=True, blank=True)
    description = models.TextField("Mô tả")
    thumbnail = models.URLField("Link ảnh thumbnail", blank=True, help_text="Link đến ảnh thumbnail project")
    icon = models.CharField("Icon class (Bootstrap/Font Awesome)", max_length=100, blank=True)
    
    # Project details
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category", related_name="projects")
    technologies = models.CharField("Công nghệ sử dụng", max_length=500, blank=True, help_text="VD: Django, React, PostgreSQL")
    duration = models.CharField("Thời gian phát triển", max_length=50, blank=True, help_text="VD: 2 tuần, 1 tháng")
    level = models.CharField("Độ khó", max_length=50, 
                           choices=[
                               ('beginner', 'Cơ bản'),
                               ('intermediate', 'Trung cấp'),
                               ('advanced', 'Nâng cao')
                           ], default='intermediate')
    
    # External links
    github_url = models.URLField("Link GitHub", blank=True)
    demo_url = models.URLField("Link Demo", blank=True)
    project_url = models.URLField("Link Project", blank=True)
    
    # Status
    is_active = models.BooleanField("Đang hoạt động", default=True)
    featured = models.BooleanField("Nổi bật", default=False)
    completed = models.BooleanField("Đã hoàn thành", default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-featured', '-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})
    
    def get_technologies_list(self):
        """Trả về list technologies."""
        if not self.technologies:
            return []
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]
    
    def __str__(self):
        return self.title


class BlogPost(models.Model):
    """Model cho bài viết blog."""
    title = models.CharField("Tiêu đề", max_length=200)
    slug = models.SlugField("Slug", unique=True, blank=True)
    content = models.TextField("Nội dung")
    excerpt = models.TextField("Tóm tắt", max_length=300, blank=True)
    featured_image = models.URLField("Link ảnh đại diện", blank=True, help_text="Link đến ảnh đại diện bài viết")
    
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
        """Trả về list tags."""
        if not self.tags:
            return []
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
    
    def __str__(self):
        return self.title


class PodcastEpisode(models.Model):
    """Model cho podcast episode."""
    title = models.CharField("Tiêu đề", max_length=200)
    slug = models.SlugField("Slug", unique=True, blank=True)
    description = models.TextField("Mô tả")
    thumbnail = models.URLField("Link ảnh thumbnail", blank=True, help_text="Link đến ảnh thumbnail episode")
    
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
    """Model cho tin nhắn liên hệ."""
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
