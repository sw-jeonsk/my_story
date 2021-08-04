from django.urls import include, path
from rest_framework import routers  # router import
from . import views  # views.py import

router = routers.DefaultRouter()  # DefaultRouter 설정
router.register("", views.WriterViewSet)  # ViewSet과 함께 user라는 router 등록

urlpatterns = [
    path("signup/", views.WriterCreate.as_view()),
    path("", include(router.urls)),
]
