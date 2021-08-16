from django.urls import include, path
from rest_framework import routers  # router import
from . import views  # views.py import

router = routers.DefaultRouter()  # DefaultRouter 설정

urlpatterns = [
    path("", views.WriterView.as_view()),
    path("/<str:pk>", views.WriterView.as_view()),
    path("/email-check", views.EmailDuplicateView.as_view()),
]
