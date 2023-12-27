from django.urls import path

from player.views import ListPlayerView, DetailPlayerView, SearchEpisodesView, add_to_queue

app_name = 'player'

urlpatterns = [
    path('episodes', ListPlayerView.as_view(), name='video_list'),
    path('video/<int:pk>/', DetailPlayerView.as_view(), name='video_detail'),
    path('search/', SearchEpisodesView.as_view(), name='search_episodes'),
    path('add_to_queue/', add_to_queue, name='add_to_queue'),
]