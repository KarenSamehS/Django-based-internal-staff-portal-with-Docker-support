from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "announcements"
    paginate_by = 5


    def get_queryset(self):
        return Post.objects.filter(
            is_published=True
        ).order_by("-created_at")


class AnnouncementListView(ListView):
    model = Post
    template_name = "posts/announcement_list.html"
    context_object_name = "announcements"
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(
            is_published=True
        ).order_by("-created_at")


class AnnouncementDetailView(DetailView):
    model = Post
    template_name = "posts/announcement_detail.html"
    context_object_name = "announcement"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "slug", "body", "is_published"]
    template_name = "posts/announcement_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy(
            "announcement-list"
        )


class AnnouncementUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView
):
    model = Post
    fields = ["title", "slug", "body", "is_published"]
    template_name = "posts/announcement_form.html"

    def test_func(self):
        return self.get_object().author == self.request.user


class AnnouncementDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, DeleteView
):
    model = Post
    template_name = "posts/announcement_confirm_delete.html"
    success_url = reverse_lazy("announcement-list")

    def test_func(self):
        return self.get_object().author == self.request.user
