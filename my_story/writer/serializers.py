import re
import pdb
from utils.exceptions import PasswordValidateException
from rest_framework import serializers  # serializer import
from .models import Writer  # 선언한 모델 import
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from utils.exceptions import EmailValidateException, NameValidateException, EmailDuplicateException
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from .validators.validate_required import validate_required
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ["id", "email", "password", "name", "created_at", "updated_at"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"validators": [validate_required]},
        }

    def validate_email(self, value):
        email = Writer.objects.filter(email=value)
        if email.exists():
            raise EmailDuplicateException
        return value

    def validate_name(self, value):

        if len(value) > 1:
            return value
        else:
            raise NameValidateException

    def validate_password(self, value):
        regex = "^(?=.*[A-Za-z])(?=.*\\d)(?=.*[~!@#$%^&*()+|=])[A-Za-z\\d~!@#$%^&*()+|=]{8,16}$"
        if not bool(re.match(regex, value)):
            raise PasswordValidateException
        return make_password(value)


class WriterLoginSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    default_error_messages = {"no_active_account": "이메일 또는 패스워드가 잘못되었습니다."}

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
