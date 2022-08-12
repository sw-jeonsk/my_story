from diary.models import Diary
from rest_framework import serializers  # serializer import


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ["writer", "title", "contents"]

