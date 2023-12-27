from django.contrib import admin

from player.models import Video, QueueItem

# Register your models here.

admin.site.register(Video)
admin.site.register(QueueItem)
