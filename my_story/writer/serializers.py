from rest_framework import serializers  # serializer import
from .models import Writer  # 선언한 모델 import
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ["id", "email", "password", "name", "created_at", "updated_at"]
        extra_kwargs = {
            "password": {"write_only": True},
        }


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
