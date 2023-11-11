from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title
