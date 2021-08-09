from django.urls import include, path
from rest_framework import routers  # router import
from . import views  # views.py import

router = routers.DefaultRouter()  # DefaultRouter 설정

urlpatterns = [
    path("", views.WriterViewSet.as_view({"post": "create"})),
    path("/<str:pk>", views.WriterViewSet.as_view({"get": "retrieve"})),
]
