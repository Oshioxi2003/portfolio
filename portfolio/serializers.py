from rest_framework import serializers

from .models import BlogPost, ContactMessage, Course, PodcastEpisode, Profile, Category


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    technologies_list = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = '__all__'
    
    def get_technologies_list(self, obj):
        return obj.get_technologies_list()


class CourseListSerializer(serializers.ModelSerializer):
    """Serializer for course list view with minimal fields."""
    category = CategorySerializer(read_only=True)
    technologies_list = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = [
            'id', 'title', 'slug', 'description', 'thumbnail', 'icon',
            'category', 'technologies', 'technologies_list', 'duration', 
            'level', 'completed', 'github_url', 'demo_url', 'featured', 'created_at'
        ]
    
    def get_technologies_list(self, obj):
        return obj.get_technologies_list()


class BlogPostSerializer(serializers.ModelSerializer):
    tags_list = serializers.SerializerMethodField()
    
    class Meta:
        model = BlogPost
        fields = '__all__'
    
    def get_tags_list(self, obj):
        return obj.get_tags_list()


class BlogPostListSerializer(serializers.ModelSerializer):
    """Serializer for blog list view with minimal fields."""
    tags_list = serializers.SerializerMethodField()
    
    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'excerpt', 'featured_image',
            'tags', 'tags_list', 'read_time', 'featured', 'published_date'
        ]
    
    def get_tags_list(self, obj):
        return obj.get_tags_list()


class PodcastEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastEpisode
        fields = '__all__'


class PodcastEpisodeListSerializer(serializers.ModelSerializer):
    """Serializer for podcast list view with minimal fields."""
    class Meta:
        model = PodcastEpisode
        fields = [
            'id', 'title', 'slug', 'description', 'thumbnail',
            'duration', 'episode_number', 'season', 'featured', 'published_date'
        ]


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        
    def create(self, validated_data):
        return ContactMessage.objects.create(**validated_data)


class HomeDataSerializer(serializers.Serializer):
    """Serializer for home page data."""
    profile = ProfileSerializer()
    featured_courses = CourseListSerializer(many=True)
    featured_posts = BlogPostListSerializer(many=True)
    latest_podcast = PodcastEpisodeListSerializer(allow_null=True)

