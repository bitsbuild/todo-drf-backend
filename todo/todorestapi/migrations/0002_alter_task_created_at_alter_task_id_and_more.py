# Generated by Django 5.2.3 on 2025-06-10 16:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todorestapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='last_updated_at',
            field=models.DateTimeField(default=None, editable=False, null=True),
        ),
    ]
