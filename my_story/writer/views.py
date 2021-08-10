from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import WriterSerializer, WriterLoginSerializer  # 생성한 serializer import
from .models import Writer  # User model import
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from drf_yasg.utils import swagger_auto_schema
from utils.exceptions import (
    EmailRequiredException,
    EmailValidateException,
    EmailDuplicateException,
    NameValidateException,
    PasswordRequiredException,
    NameRequiredException,
)

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class WriterViewSet(viewsets.ModelViewSet):  # ModelViewSet 활용
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    permission_classes_by_action = {"create": [AllowAny], "retrieve": [IsAuthenticated]}

    def retrieve(self, request, pk=None):
        writer = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(writer)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="회원가입",
        responses={
            400: EmailValidateException.as_md()
            + EmailDuplicateException.as_md()
            + NameValidateException.as_md()
        },
    )
    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        # 요청 데이터의 필수로 필요한 데이터에 대한 예외처리
        self.validate_field_check(request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            "{} create successfully".format(serializer.data["name"]),
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def validate_field_check(self, data):

        if not "email" in data.keys() or len(data["email"]) < 1:
            raise EmailRequiredException
        elif not "password" in data.keys() or len(data["password"]) < 1:
            raise PasswordRequiredException
        elif not "name" in data.keys() or len(data["name"]) < 1:
            raise NameRequiredException

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class WriterLogInView(TokenObtainPairView):
    serializer_class = WriterLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        post 오버라이드 해서 유저가 있을때, 패스워드가 다를 때 예외처리 구분
        """
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
