from django.urls import path

from player.views import *

app_name = 'player'

urlpatterns = [
    path('episodes', ListPlayerView.as_view(), name='video_list'),
    path('video/<int:pk>/', DetailPlayerView.as_view(), name='video_detail'),
    path('search/', SearchEpisodesView.as_view(), name='search_episodes'),
    path('add_to_queue/', add_to_queue, name='add_to_queue'),
    path('saved_episodes/', list_queue_items, name='list_queue_items'),
    path('remove_from_queue/', remove_from_queue, name='remove_from_queue'),

]