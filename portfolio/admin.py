from django.contrib import admin
from .models import Profile, Course, BlogPost, PodcastEpisode, ContactMessage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'total_students', 'total_views', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'email', 'tagline']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Thông tin cá nhân', {
            'fields': ('name', 'tagline', 'bio', 'avatar', 'email', 'phone')
        }),
        ('Mạng xã hội', {
            'fields': ('facebook_url', 'instagram_url', 'youtube_url', 'linkedin_url'),
            'classes': ('collapse',)
        }),
        ('Thống kê', {
            'fields': ('total_students', 'total_views', 'years_experience', 'courses_created')
        }),
        ('Thời gian', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'level', 'price', 'is_active', 'featured', 'created_at']
    list_filter = ['level', 'is_active', 'featured', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_active', 'featured']
    
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('title', 'slug', 'description', 'thumbnail', 'icon')
        }),
        ('Chi tiết khóa học', {
            'fields': ('duration', 'level', 'price', 'course_url', 'enrollment_required')
        }),
        ('Trạng thái', {
            'fields': ('is_active', 'featured')
        }),
        ('Thời gian', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published', 'featured', 'published_date', 'read_time']
    list_filter = ['is_published', 'featured', 'published_date']
    search_fields = ['title', 'content', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['published_date', 'updated_at']
    list_editable = ['is_published', 'featured']
    date_hierarchy = 'published_date'
    
    fieldsets = (
        ('Nội dung', {
            'fields': ('title', 'slug', 'excerpt', 'content', 'featured_image')
        }),
        ('Meta', {
            'fields': ('tags', 'read_time')
        }),
        ('Trạng thái', {
            'fields': ('is_published', 'featured')
        }),
        ('Thời gian', {
            'fields': ('published_date', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(PodcastEpisode)
class PodcastEpisodeAdmin(admin.ModelAdmin):
    list_display = ['title', 'episode_number', 'season', 'duration', 'is_published', 'featured']
    list_filter = ['season', 'is_published', 'featured', 'published_date']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['published_date', 'updated_at']
    list_editable = ['is_published', 'featured']
    ordering = ['-episode_number']
    
    fieldsets = (
        ('Thông tin episode', {
            'fields': ('title', 'slug', 'description', 'thumbnail', 'episode_number', 'season')
        }),
        ('Media', {
            'fields': ('audio_url', 'video_embed_url', 'duration')
        }),
        ('Links ngoài', {
            'fields': ('spotify_url', 'apple_url', 'youtube_url'),
            'classes': ('collapse',)
        }),
        ('Trạng thái', {
            'fields': ('is_published', 'featured')
        }),
        ('Thời gian', {
            'fields': ('published_date', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'is_replied', 'created_at']
    list_filter = ['is_read', 'is_replied', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    list_editable = ['is_read', 'is_replied']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Thông tin liên hệ', {
            'fields': ('name', 'email', 'subject')
        }),
        ('Nội dung', {
            'fields': ('message',)
        }),
        ('Trạng thái', {
            'fields': ('is_read', 'is_replied')
        }),
        ('Thời gian', {
            'fields': ('created_at',)
        }),
    )
    
    def get_queryset(self, request):
        """Hiển thị tin nhắn chưa đọc đầu tiên"""
        qs = super().get_queryset(request)
        return qs.order_by('is_read', '-created_at')


# Tùy chỉnh admin site
admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Quản lý Portfolio"
