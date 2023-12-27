from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title


class QueueItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    episode = models.ForeignKey(Video, on_delete=models.CASCADE)  # Zastąp to modelem, który używasz
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'episode')

    def __str__(self):
        return f'{self.user.username} - {self.episode.title}'