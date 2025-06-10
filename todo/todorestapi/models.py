from django.db import models
class Task(models.Model):
    task_name = models.CharField(max_length=70)
    task_description = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    created_at  = models.DateTimeField()
    due_at = models.DateTimeField(null=True)
    last_updated_at = models.DateField()
    def __str__(self):
        return self.task_name