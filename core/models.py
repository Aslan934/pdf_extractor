from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    filePdf = models.FileField(blank=False, null=False)
    content = models.TextField()
    task_id = models.CharField(max_length=50)
