from diary.serializers import DiarySerializer
from rest_framework import viewsets, status, permissions, response
from .models import Diary
from utils.exceptions import CreateSuccess

# Create your views here.


class DiaryView(viewsets.ModelViewSet):  # ModelViewSet 활용
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
        "retrieve": [permissions.IsAuthenticated],
    }

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
