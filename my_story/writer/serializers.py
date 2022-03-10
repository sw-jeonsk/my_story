import re
from utils.response_detail import ResponseDetail
from rest_framework import serializers  # serializer import
from .models import Writer  # 선언한 모델 import
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from utils.exceptions import PasswordValidateException


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ["id", "email", "password", "name", "created_at", "updated_at"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_password(self, password):
        regex = "^(?=.*[A-Za-z])(?=.*\\d)(?=.*[~!@#$%^&*()+|=])[A-Za-z\\d~!@#$%^&*()+|=]{8,16}$"
        if not bool(re.match(regex, password)):
            raise PasswordValidateException
        return make_password(password)


class WriterLoginSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    default_error_messages = {"no_active_account": ResponseDetail.LOGIN_VALIDATE}

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["name"] = user.name
        # Add more custom fields from your custom user model, If you have a
        # custom user model.
        # ...
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["id"] = str(self.user.id)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ["email"]
