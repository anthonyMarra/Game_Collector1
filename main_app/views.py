from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_list(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})

def games_detail(request, game_id):
    game = game.objects.get(id=game_id)
    # instantiate FeedingForm to be rendered within
    # the detail.html template
    return render(request, 'games/detail.html', {
    'game': game,
    })

class GameCreate(CreateView):
    model = Game
    fields = ['name', 'genre', 'description', 'hoursPlayed']
    # This inherited method is called when a
    # valid game form is being submitted


class GameUpdate(UpdateView):
    model = Game
    fields = ['description', 'hoursPlayed']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'