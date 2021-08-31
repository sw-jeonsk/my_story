from django.urls import path
from rest_framework import routers  # router import
from . import views  # views.py import

router = routers.DefaultRouter()  # DefaultRouter 설정

urlpatterns = [
    path("", views.DiaryView.as_view({"post": "create", "get": "list"})),
]
