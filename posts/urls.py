from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path("", views.announcement_list, name="announcement-list"),
    path("<slug:slug>/", views.announcement_detail, name="announcement-detail"),
  
]
