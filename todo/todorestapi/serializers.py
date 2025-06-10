from rest_framework import serializers
class TaskSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    task_name = serializers.CharField()
    task_description = serializers.CharField()
    is_completed = serializers.BooleanField()
    created_at  = serializers.DateTimeField()
    due_at = serializers.DateTimeField()
    last_updated_at = serializers.DateTimeField()