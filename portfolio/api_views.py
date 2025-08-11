from django.db.models import Q
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import BlogPost, ContactMessage, Course, PodcastEpisode, Profile, Category
from .serializers import (
    BlogPostListSerializer,
    BlogPostSerializer,
    CategorySerializer,
    ContactMessageSerializer,
    CourseListSerializer,
    CourseSerializer,
    HomeDataSerializer,
    PodcastEpisodeListSerializer,
    PodcastEpisodeSerializer,
    ProfileSerializer,
)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


@api_view(['GET'])
def profile_view(request):
    """Get profile information."""
    try:
        profile = Profile.objects.first()
        if profile:
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        return Response({'detail': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def home_data_view(request):
    """Get data for home page."""
    try:
        profile = Profile.objects.first()
        featured_courses = Course.objects.filter(featured=True, is_active=True)[:3]
        featured_posts = BlogPost.objects.filter(featured=True, is_published=True)[:3]
        latest_podcast = PodcastEpisode.objects.filter(is_published=True).first()
        
        data = {
            'profile': profile,
            'featured_courses': featured_courses,
            'featured_posts': featured_posts,
            'latest_podcast': latest_podcast,
        }
        
        serializer = HomeDataSerializer(data)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CourseListView(generics.ListAPIView):
    """List all courses with filtering."""
    serializer_class = CourseListSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        queryset = Course.objects.filter(is_active=True).order_by('-featured', '-created_at')
        
        # Filter by category
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)
            
        # Filter by level
        level = self.request.query_params.get('level')
        if level:
            queryset = queryset.filter(level=level)
            
        # Filter by technology
        tech = self.request.query_params.get('tech')
        if tech:
            queryset = queryset.filter(technologies__icontains=tech)
            
        return queryset


class CourseDetailView(generics.RetrieveAPIView):
    """Get course details by slug."""
    serializer_class = CourseSerializer
    lookup_field = 'slug'
    
    def get_queryset(self):
        return Course.objects.filter(is_active=True)


@api_view(['GET'])
def categories_view(request):
    """Get all categories."""
    try:
        categories = Category.objects.filter(is_active=True)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def technologies_view(request):
    """Get all technologies."""
    try:
        all_projects = Course.objects.filter(is_active=True).exclude(technologies='')
        all_technologies = set()
        for project in all_projects:
            all_technologies.update(project.get_technologies_list())
        return Response(sorted(all_technologies))
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def featured_courses_view(request):
    """Get featured courses."""
    try:
        courses = Course.objects.filter(featured=True, is_active=True)[:6]
        serializer = CourseListSerializer(courses, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BlogPostListView(generics.ListAPIView):
    """List all blog posts with search and filtering"""
    serializer_class = BlogPostListSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        queryset = BlogPost.objects.filter(is_published=True).order_by('-published_date')
        
        # Search functionality
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(content__icontains=search_query) |
                Q(tags__icontains=search_query)
            )
        
        # Tag filtering
        tag = self.request.query_params.get('tag')
        if tag:
            queryset = queryset.filter(tags__icontains=tag)
            
        return queryset


class BlogPostDetailView(generics.RetrieveAPIView):
    """Get blog post details by slug"""
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    
    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


@api_view(['GET'])
def featured_blog_posts_view(request):
    """Get featured blog posts"""
    try:
        posts = BlogPost.objects.filter(featured=True, is_published=True)[:6]
        serializer = BlogPostListSerializer(posts, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def blog_tags_view(request):
    """Get all blog tags."""
    try:
        all_posts = BlogPost.objects.filter(is_published=True).exclude(tags='')
        all_tags = set()
        for post in all_posts:
            all_tags.update(post.get_tags_list())
        return Response(sorted(all_tags))
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PodcastEpisodeListView(generics.ListAPIView):
    """List all podcast episodes with filtering"""
    serializer_class = PodcastEpisodeListSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        queryset = PodcastEpisode.objects.filter(is_published=True).order_by('-episode_number')
        
        season = self.request.query_params.get('season')
        if season:
            queryset = queryset.filter(season=season)
            
        return queryset


class PodcastEpisodeDetailView(generics.RetrieveAPIView):
    """Get podcast episode details by slug"""
    serializer_class = PodcastEpisodeSerializer
    lookup_field = 'slug'
    
    def get_queryset(self):
        return PodcastEpisode.objects.filter(is_published=True)


@api_view(['GET'])
def featured_podcast_episodes_view(request):
    """Get featured podcast episodes"""
    try:
        episodes = PodcastEpisode.objects.filter(featured=True, is_published=True)[:6]
        serializer = PodcastEpisodeListSerializer(episodes, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def podcast_seasons_view(request):
    """Get all podcast seasons"""
    try:
        seasons = PodcastEpisode.objects.filter(
            is_published=True
        ).values_list('season', flat=True).distinct().order_by('season')
        return Response(list(seasons))
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def contact_view(request):
    """Handle contact form submission."""
    if request.method == 'POST':
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Cảm ơn bạn đã liên hệ! Tôi sẽ phản hồi sớm nhất có thể.'}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'detail': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

