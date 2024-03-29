from django.urls import path
from rest_framework import routers  # router import
from . import views  # views.py import

router = routers.DefaultRouter()  # DefaultRouter 설정

urlpatterns = [
    path("", views.WriterView.as_view({"post": "create", "get": "retrieve"})),
    path("/email-check", views.EmailDupView.as_view()),
]
