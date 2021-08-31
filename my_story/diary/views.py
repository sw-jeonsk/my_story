from django.shortcuts import get_object_or_404
from diary.serializers import DiarySerializer
from rest_framework import viewsets, status, permissions, response
from .models import Diary
from utils.exceptions import CreateSuccess
from writer.models import Writer
from utils.serializers import ListSerializer
from utils.list_object import ListObject
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


class DiaryView(viewsets.ModelViewSet):  # ModelViewSet 활용
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
        "list": [permissions.IsAuthenticated],
    }

    param_writer_id = openapi.Parameter(
        "id",
        openapi.IN_QUERY,
        description="writer id value",
        type=openapi.TYPE_STRING,
    )

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        return response.Response(
            CreateSuccess.json_data("diary 생성 성공"),
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    @swagger_auto_schema(
        manual_parameters=[param_writer_id],
    )
    def list(self, request):
        id = self.request.query_params.get("id", None)
        writer = get_object_or_404(Writer, pk=id)
        diary = self.queryset.filter(writer=writer)
        serializer = self.get_serializer(diary, many=True)

        list_serializer = ListSerializer(
            ListObject(status_code=200, detail="ok", items=serializer.data)
        )
        return response.Response(list_serializer.data)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
