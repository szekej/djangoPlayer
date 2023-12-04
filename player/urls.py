from django.urls import path

from player.views import ListPlayerView, DetailPlayerView

app_name = 'player'

urlpatterns = [
    path('episodes', ListPlayerView.as_view(), name='video_list'),
    path('video/<int:pk>/', DetailPlayerView.as_view(), name='video_detail')
]