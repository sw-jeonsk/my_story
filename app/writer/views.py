from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets  # vieset import
from .serializers import WriterSerializer  # 생성한 serializer import
from .models import Writer  # User model import

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class WriterCreate(generics.CreateAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer


class WriterViewSet(viewsets.ModelViewSet):  # ModelViewSet 활용
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
