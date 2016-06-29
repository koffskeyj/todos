from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)
    order = models.IntegerField(null=True, blank=True)