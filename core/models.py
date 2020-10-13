from django.db import models


class File(models.Model):
    filePdf = models.FileField(blank=False, null=False)
    content = models.TextField()
    task_id = models.CharField(max_length=50)
