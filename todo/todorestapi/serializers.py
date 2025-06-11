from rest_framework import serializers
class TaskSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    task_name = serializers.CharField()
    task_description = serializers.CharField()
    is_completed = serializers.BooleanField()
    created_at  = serializers.DateTimeField()

class AddSerializer(serializers.Serializer):
    name = serializers.CharField()
    desc = serializers.CharField()

class UpdateSerializer(serializers.Serializer):
    name = serializers.CharField()
    desc = serializers.CharField()  