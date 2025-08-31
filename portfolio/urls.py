from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home_view, name='home'),
    
    # About page
    path('about/', views.about_view, name='about'),
    
    # Courses (Projects)
    path('courses/', views.courses_view, name='courses'),
    path('courses/<slug:slug>/', views.course_detail_view, name='course_detail'),
    
    # Blog
    path('blog/', views.blog_view, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail_view, name='blog_detail'),
    
    # Podcast
    path('podcast/', views.podcast_view, name='podcast'),
    path('podcast/<slug:slug>/', views.podcast_detail_view, name='podcast_detail'),
    
    # Contact
    path('contact/', views.contact_view, name='contact'),
    
    # CV Download
    path('download-cv/', views.download_cv, name='download_cv'),
]