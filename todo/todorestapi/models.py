import uuid
from django.db import models
from django.utils import timezone
class Task(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    task_name = models.CharField(max_length=70)
    task_description = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    created_at  = models.DateTimeField(editable=False,default=timezone.now)
    def __str__(self):
        return self.task_name