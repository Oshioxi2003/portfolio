from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.conf import settings
import os
import mimetypes

from .forms import ContactForm
from .models import BlogPost, ContactMessage, Course, PodcastEpisode, Profile, Category


def home_view(request):
    """Trang Home với profile và thống kê."""
    profile = Profile.objects.first()
    
    # Lấy một số items nổi bật
    featured_courses = Course.objects.filter(featured=True, is_active=True)[:3]
    featured_posts = BlogPost.objects.filter(featured=True, is_published=True)[:3]
    latest_podcast = PodcastEpisode.objects.filter(is_published=True).first()
    
    context = {
        'profile': profile,
        'featured_courses': featured_courses,
        'featured_posts': featured_posts,
        'latest_podcast': latest_podcast,
    }
    return render(request, 'portfolio/home.html', context)


def about_view(request):
    """Trang About với thông tin cá nhân chi tiết."""
    profile = Profile.objects.first()
    
    context = {
        'profile': profile,
    }
    return render(request, 'portfolio/about.html', context)


def courses_view(request):
    """Trang danh sách projects."""
    projects = Course.objects.filter(is_active=True).order_by('-featured', '-created_at')
    
    # Lọc theo category
    category_slug = request.GET.get('category')
    if category_slug:
        projects = projects.filter(category__slug=category_slug)
    
    # Lọc theo level nếu có
    level = request.GET.get('level')
    if level:
        projects = projects.filter(level=level)
    
    # Lọc theo technology
    tech = request.GET.get('tech')
    if tech:
        projects = projects.filter(technologies__icontains=tech)
    
    # Phân trang
    paginator = Paginator(projects, 9)  # 9 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Lấy categories để hiển thị filter
    categories = Category.objects.filter(is_active=True)
    
    # Lấy tất cả technologies để hiển thị filter
    all_projects = Course.objects.filter(is_active=True).exclude(technologies='')
    all_technologies = set()
    for project in all_projects:
        all_technologies.update(project.get_technologies_list())
    
    context = {
        'page_obj': page_obj,
        'current_level': level,
        'current_category': category_slug,
        'current_tech': tech,
        'categories': categories,
        'technologies': sorted(all_technologies),
    }
    return render(request, 'portfolio/courses.html', context)


def course_detail_view(request, slug):
    """Trang chi tiết project."""
    project = get_object_or_404(Course, slug=slug, is_active=True)
    related_projects = Course.objects.filter(
        is_active=True, category=project.category
    ).exclude(id=project.id)[:3]
    
    context = {
        'course': project,  # Giữ tên 'course' để không phải đổi template
        'project': project,
        'related_courses': related_projects,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio/course_detail.html', context)


def blog_view(request):
    """Trang blog với filter và search."""
    posts = BlogPost.objects.filter(is_published=True)
    
    # Tìm kiếm
    search_query = request.GET.get('search')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query) |
            Q(tags__icontains=search_query)
        )
    
    # Lọc theo tag
    tag = request.GET.get('tag')
    if tag:
        posts = posts.filter(tags__icontains=tag)
    
    # Phân trang
    paginator = Paginator(posts, 6)  # 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Lấy tất cả tags để hiển thị filter
    all_posts = BlogPost.objects.filter(is_published=True).exclude(tags='')
    all_tags = set()
    for post in all_posts:
        all_tags.update(post.get_tags_list())
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'current_tag': tag,
        'all_tags': sorted(all_tags),
        'featured_posts': BlogPost.objects.filter(featured=True, is_published=True)[:3],
    }
    return render(request, 'portfolio/blog.html', context)


def blog_detail_view(request, slug):
    """Trang chi tiết bài viết."""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    related_posts = BlogPost.objects.filter(
        is_published=True
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'portfolio/blog_detail.html', context)


def podcast_view(request):
    """Trang podcast episodes."""
    episodes = PodcastEpisode.objects.filter(is_published=True)
    
    # Lọc theo season
    season = request.GET.get('season')
    if season:
        episodes = episodes.filter(season=season)
    
    # Phân trang
    paginator = Paginator(episodes, 8)  # 8 episodes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Lấy tất cả seasons
    seasons = PodcastEpisode.objects.filter(
        is_published=True
    ).values_list('season', flat=True).distinct().order_by('season')
    
    context = {
        'page_obj': page_obj,
        'current_season': season,
        'seasons': seasons,
        'featured_episodes': PodcastEpisode.objects.filter(featured=True, is_published=True)[:3],
    }
    return render(request, 'portfolio/podcast.html', context)


def podcast_detail_view(request, slug):
    """Trang chi tiết podcast episode."""
    episode = get_object_or_404(PodcastEpisode, slug=slug, is_published=True)
    related_episodes = PodcastEpisode.objects.filter(
        is_published=True, season=episode.season
    ).exclude(id=episode.id)[:3]
    
    context = {
        'episode': episode,
        'related_episodes': related_episodes,
    }
    return render(request, 'portfolio/podcast_detail.html', context)


def contact_view(request):
    """Trang liên hệ với form."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Lưu tin nhắn
            contact_message = ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            messages.success(request, 'Cảm ơn bạn đã liên hệ! Tôi sẽ phản hồi sớm nhất có thể.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    # Lấy thông tin profile để hiển thị thông tin liên hệ
    profile = Profile.objects.first()
    
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'portfolio/contact.html', context)


def download_cv(request):
    """Download CV file."""
    # Đường dẫn đến file CV
    cv_path = os.path.join(settings.MEDIA_ROOT, 'profile', 'CV', 'DAO-HUY-TOAN-REACT-DEV-TA.pdf')
    
    # Kiểm tra file có tồn tại không
    if not os.path.exists(cv_path):
        raise Http404("CV file not found")
    
    # Xác định content type
    content_type, _ = mimetypes.guess_type(cv_path)
    if content_type is None:
        content_type = 'application/pdf'
    
    # Đọc file và trả về response
    with open(cv_path, 'rb') as cv_file:
        response = HttpResponse(cv_file.read(), content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="DAO-HUY-TOAN-REACT-DEV-TA.pdf"'
        response['Content-Length'] = os.path.getsize(cv_path)
        return response
