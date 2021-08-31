from rest_framework import serializers  # serializer import


class ListSerializer(serializers.Serializer):
    status_code = serializers.IntegerField(required=True)
    detail = serializers.CharField(required=True)
    items = serializers.ListField(required=True)
