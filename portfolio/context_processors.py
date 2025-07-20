from .models import Profile


def profile_context(request):
    """Context processor để truyền profile vào tất cả templates"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    return {
        'profile': profile
    } 