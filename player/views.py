import requests
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from player.models import Video


# Create your views here.


class ListPlayerView(ListView):
    model = Video
    template_name = 'player/episodes_list.html'
    context_object_name = 'episodes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        per_page = int(self.request.GET.get('per_page', 50))  # Pobieranie wybranej liczby odcinków
        paginator = Paginator(context['episodes'], per_page)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'episodes': page_obj,
            'per_page': per_page
        }
        return context


class DetailPlayerView(DetailView):
    model = Video
    template_name = 'player/episode_detail.html'
    context_object_name = 'video'

    def get_object(self, queryset=None):
        return get_object_or_404(Video, pk=self.kwargs['pk'])