
from django.urls import path
from .views import (
    AnnouncementListView,
    AnnouncementDetailView,
    AnnouncementCreateView,
    AnnouncementUpdateView,
    AnnouncementDeleteView,
)

urlpatterns = [
    path("", AnnouncementListView.as_view(), name="announcement-list"),
    path("create/", AnnouncementCreateView.as_view(), name="announcement-create"),
    path("<slug:slug>/edit/", AnnouncementUpdateView.as_view(), name="announcement-update"),
    path("<slug:slug>/delete/", AnnouncementDeleteView.as_view(), name="announcement-delete"),
    path("<slug:slug>/", AnnouncementDetailView.as_view(), name="announcement-detail"),
]
