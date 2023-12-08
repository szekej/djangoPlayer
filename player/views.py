import requests
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from player.models import Video


# Create your views here.

from .models import Video


def get_available_episodes(request):
    episodes = list(Video.objects.values_list('pk', flat=True))
    return {'available_episodes': episodes}


def search_episodes(request):
    if request.method == "POST":
        search_input = request.POST.get('search_input', '').lower()
        episodes = Video.objects.all()
        matching_episodes = [episode for episode in episodes if search_input in episode.title.lower()]

        if not matching_episodes:
            matching_episodes = ['brak odcinków']

    return render(request, template_name='player/searched_episodes.html', context={'matching_episodes': matching_episodes})


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