from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def home(request):
    announcements = Post.objects.filter(is_published=True).order_by("-created_at")[:5]
    return render(
        request,
        "home.html",
        {"announcements": announcements},
    )


def announcement_list(request):
    announcements = Post.objects.filter(is_published=True).order_by("-created_at")
    return render(
        request,
        "posts/announcement_list.html",
        {"announcements": announcements},
    )


def announcement_detail(request, slug):
    announcement = get_object_or_404(Post, slug=slug, is_published=True)
    return render(
        request,
        "posts/announcement_detail.html",
        {"announcement": announcement},
    )
