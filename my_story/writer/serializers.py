from rest_framework import serializers  # serializer import
from .models import Writer  # 선언한 모델 import
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from utils.exceptions import EmailValidateException, NameValidateException


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

    def validate_name(self, value):

        if len(value) > 1:
            return value
        else:
            raise NameValidateException("이름이 잘못되었습니다.")

    def validate_email(self, value):
        try:
            validate_email(value)
            return value
        except ValidationError as email_validate:
            raise EmailValidateException("이메일이 잘못되었습니다.") from email_validate