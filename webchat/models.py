from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    topic = models.TextField(max_length=255)
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
