from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    role = serializers.CharField(required=True)
    content = serializers.CharField(required=True)


class AssistantResponseSerializer(serializers.Serializer):
    assistant_response = serializers.CharField()
