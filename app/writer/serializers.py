from rest_framework import serializers  # serializer import
from .models import Writer  # 선언한 모델 import


class WriterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(allow_null=False, required=True)
    name = serializers.CharField(allow_null=False, required=True)
    password = serializers.CharField(allow_null=False, required=True)

    def create(self, validated_data):

        writer = Writer.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )
        return writer

    class Meta:
        model = Writer  # 모델 설정
        fields = ("email", "name", "password", "created_at")  # 필드 설정
