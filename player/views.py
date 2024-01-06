import json

import requests
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse

# Create your views here.
from .models import Video, QueueItem


def get_available_episodes(request):
    episodes = list(Video.objects.values_list('pk', flat=True))
    return {'available_episodes': episodes}


@login_required
def add_to_queue(request):
    if request.method == 'POST' :
        episode_pk = request.POST.get('episode_pk')

        # Sprawdź, czy użytkownik jest zalogowany
        if request.user.is_authenticated:
            # Sprawdź, czy odcinek już nie istnieje w kolejce użytkownika
            if not QueueItem.objects.filter(user=request.user, episode_id=episode_pk).exists():
                # Dodaj odcinek do kolejki
                QueueItem.objects.create(user=request.user, episode_id=episode_pk)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'message': 'Odcinek już jest w kolejce.'})
        else:
            return JsonResponse({'success': False, 'message': 'Użytkownik nie jest zalogowany.'})

    return JsonResponse({'success': False, 'message': 'Błąd żądania.'})


def list_queue_items(request):
    # Pobierz wszystkie obiekty QueueItem powiązane z zalogowanym użytkownikiem
    queue_items = QueueItem.objects.all()

    # Pobierz dane odcinków (tytuł i link) dla każdego obiektu QueueItem
    videos_data = [{'title': item.episode.title,
                    'url': item.episode.video_url,
                    'description': item.episode.description} for item in queue_items]

    return render(request, 'player/list_queue_items.html', {'videos_data': videos_data})


def remove_from_queue(request):
    if request.method == 'POST':
        episode_pk = request.POST.get('episode_pk')
        try:
            queue_item = QueueItem.objects.get(user=request.user, episode_id=episode_pk)
            queue_item.delete()
            messages.success(request, 'Odcinek został usunięty z kolejki.')
        except QueueItem.DoesNotExist:
            messages.error(request, 'Odcinek nie znajduje się w kolejce.')

    return redirect(request.META.get('HTTP_REFERER', 'player:video_list'))      # previous page or 'player:video_list'


class SearchEpisodesView(View):
    template_name = 'player/searched_episodes.html'

    def post(self, request, *args, **kwargs):
        search_input = self.request.POST.get('search_input', '').lower()
        episodes = Video.objects.all()
        matching_episodes = [episode for episode in episodes if search_input in episode.title.lower()]

        if not matching_episodes:
            matching_episodes = ['brak odcinków']

        return render(request, template_name=self.template_name, context={'matching_episodes': matching_episodes})

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name, context={})


class ListPlayerView(ListView):
    model = Video
    template_name = 'player/episodes_list.html'
    context_object_name = 'episodes'

    def get_context_data(self, **kwargs):
        queued_episodes = QueueItem.objects.all()
        queued_episodes = [item.episode.title for item in queued_episodes]
        context = super().get_context_data(**kwargs)
        per_page = int(self.request.GET.get('per_page', 50))  # Pobieranie wybranej liczby odcinków
        paginator = Paginator(context['episodes'], per_page)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'episodes': page_obj,
            'per_page': per_page,
            'queued_episodes': queued_episodes
        }
        return context


class DetailPlayerView(DetailView):
    model = Video
    template_name = 'player/episode_detail.html'
    context_object_name = 'video'

    def get_object(self, queryset=None):
        return get_object_or_404(Video, pk=self.kwargs['pk'])