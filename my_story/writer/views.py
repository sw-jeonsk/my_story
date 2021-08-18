from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import (
    WriterSerializer,
    WriterLoginSerializer,
    EmailSerializer,
)  # 생성한 serializer import
from .models import Writer  # User model import
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from utils.exceptions import (
    EmailRequiredException,
    EmailValidateException,
    EmailDuplicateException,
    NameValidateException,
    PasswordRequiredException,
    NameRequiredException,
    UnauthorizedException,
    NotFoundWriterException,
    CreateSuccess,
)
from drf_yasg import openapi


# Create your views here.


class WriterView(viewsets.ModelViewSet):  # ModelViewSet 활용
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    permission_classes_by_action = {"create": [AllowAny], "retrieve": [IsAuthenticated]}

    param_writer_id = openapi.Parameter(
        "id",
        openapi.IN_QUERY,
        description="writer id value",
        type=openapi.TYPE_STRING,
    )

    @swagger_auto_schema(
        manual_parameters=[param_writer_id],
        operation_description="로그인",
        responses={
            400: EmailRequiredException.as_md(["email"])
            + PasswordRequiredException.as_md(["password"]),
            401: UnauthorizedException.as_md(),  # 권한 문제
            404: NotFoundWriterException.as_md(),  # writer 유저 없어서 발생하는 문제
        },
    )
    def retrieve(self, request, pk=None):

        writer = get_object_or_404(self.get_queryset(), pk=request.GET["id"])
        serializer = self.get_serializer(writer)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="회원가입",
        responses={
            400: EmailValidateException.as_md()
            + EmailDuplicateException.as_md()
            + NameValidateException.as_md()
            + EmailRequiredException.as_md(["email"])
            + PasswordRequiredException.as_md(["password"])
            + NameRequiredException.as_md(["name"])
        },
    )
    def create(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            CreateSuccess.json_data("Writer 생성 성공"),
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

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

    @swagger_auto_schema(
        operation_description="로그인",
        responses={
            400: EmailRequiredException.as_md(["email"])  # 이메일 필수
            + PasswordRequiredException.as_md(["password"]),  # 패스워드 필수
            401: UnauthorizedException.as_md(),  # 권한 문제
        },
    )
    def post(self, request, *args, **kwargs):
        """
        post 오버라이드 해서 유저가 있을때, 패스워드가 다를 때 예외처리 구분
        """
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:

            raise InvalidToken(e.args[0]) from e

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class EmailDupView(generics.GenericAPIView):
    serializer_class = EmailSerializer

    @swagger_auto_schema(
        operation_description="이메일 중복체크",
        responses={
            400: EmailRequiredException.as_md(["email"])
            + EmailDuplicateException.as_md(),  # 이메일 필수
        },
    )
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                Writer.objects.get(email=serializer.data["email"])
                raise EmailDuplicateException
            except Writer.DoesNotExist:
                return Response("ok", status=status.HTTP_200_OK)

        else:
            raise EmailRequiredException
