from diary.models import Diary
from rest_framework import serializers  # serializer import


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ["writer", "title", "contents"]

    # def validate_writer(self, writer):
    #     writer = get_object_or_404(Writer, pk=writer)
    #     return writer
