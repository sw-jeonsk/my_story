from rest_framework import serializers, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import (
    WriterSerializer,
    WriterLoginSerializer,
    WriterEmailSerializer,
)  # 생성한 serializer import
from .models import Writer  # User model import
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework import mixins

from utils.exceptions import (
    EmailRequiredException,
    EmailValidateException,
    EmailDuplicateException,
    NameValidateException,
    PasswordRequiredException,
    NameRequiredException,
    UnauthorizedException,
    NotFoundWriterException,
)

from .validators import validate_required_check

# Create your views here.


class WriterView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):  # ModelViewSet 활용
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    # permission_classes_by_action = {"create": [AllowAny], "retrieve": [IsAuthenticated]}
    # permission_classes_by_action = {"post": [AllowAny], "get": [IsAuthenticated]}

    @swagger_auto_schema(
        operation_description="로그인",
        responses={
            400: EmailRequiredException.as_md() + PasswordRequiredException.as_md(),
            401: UnauthorizedException.as_md(),  # 권한 문제
            404: NotFoundWriterException.as_md(),  # writer 유저 없어서 발생하는 문제
        },
    )
    @permission_classes([IsAuthenticated])
    def get(self, request, pk=None):
        writer = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(writer)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="회원가입",
        responses={
            400: EmailValidateException.as_md()
            + EmailDuplicateException.as_md()
            + NameValidateException.as_md()
            + EmailRequiredException.as_md()
            + PasswordRequiredException.as_md()
            + NameRequiredException.as_md()
        },
    )
    @permission_classes([AllowAny])
    def post(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            "{} create successfully".format(serializer.data["name"]),
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    # def get_permissions(self):
    #     try:
    #         # return permission_classes depending on `action`
    #         return [permission() for permission in self.permission_classes_by_action[self.action]]
    #     except KeyError:
    #         # action is not set return default permission_classes
    #         return [permission() for permission in self.permission_classes]


class WriterLogInView(TokenObtainPairView):
    serializer_class = WriterLoginSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="로그인",
        responses={
            400: EmailRequiredException.as_md()  # 이메일 필수
            + PasswordRequiredException.as_md(),  # 패스워드 필수
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


class EmailDuplicateView(generics.GenericAPIView):
    permission_classes = [
        AllowAny,
    ]
    serializer_class = WriterEmailSerializer

    def post(self, request, *args, **kwargs):
        import pdb

        pdb.set_trace()
        serializer = self.get_serializer(data=request.data)

        # email, parameter check
        serializer.is_valid(raise_exception=True)

        writer = Writer.objects.filter(email=request.data.get("email", None))

        if writer is None:
            return Response(status=status.HTTP_200_OK)
        else:
            raise EmailDuplicateException
