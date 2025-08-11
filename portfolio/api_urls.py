from django.urls import path
from . import api_views

urlpatterns = [
    # Profile
    path('profile/', api_views.profile_view, name='api-profile'),
    
    # Home data
    path('home/', api_views.home_data_view, name='api-home'),
    
    # Categories
    path('categories/', api_views.categories_view, name='api-categories'),
    path('technologies/', api_views.technologies_view, name='api-technologies'),
    
    # Courses/Projects
    path('courses/', api_views.CourseListView.as_view(), name='api-courses'),
    path('courses/featured/', api_views.featured_courses_view, name='api-featured-courses'),
    path('courses/<slug:slug>/', api_views.CourseDetailView.as_view(), name='api-course-detail'),
    
    # Blog
    path('blog/', api_views.BlogPostListView.as_view(), name='api-blog'),
    path('blog/featured/', api_views.featured_blog_posts_view, name='api-featured-blog'),
    path('blog/tags/', api_views.blog_tags_view, name='api-blog-tags'),
    path('blog/<slug:slug>/', api_views.BlogPostDetailView.as_view(), name='api-blog-detail'),
    
    # Podcast
    path('podcast/', api_views.PodcastEpisodeListView.as_view(), name='api-podcast'),
    path('podcast/featured/', api_views.featured_podcast_episodes_view, name='api-featured-podcast'),
    path('podcast/seasons/', api_views.podcast_seasons_view, name='api-podcast-seasons'),
    path('podcast/<slug:slug>/', api_views.PodcastEpisodeDetailView.as_view(), name='api-podcast-detail'),
    
    # Contact
    path('contact/', api_views.contact_view, name='api-contact'),
]

