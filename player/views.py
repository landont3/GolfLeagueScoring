from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import PlayerRound, Week
from .forms import PlayerRoundForm


@login_required()
def welcome(request):
    return render(request, r'..\templates\player\welcome.html')


@login_required()
def score_entry(request):
    form = PlayerRoundForm()
    return render(request, r'..\templates\player\score_entry.html', {'form': form})


@login_required()
def score_edit(request, player_round_id):
    player_round = PlayerRound.objects.filter(id=player_round_id)
    form = PlayerRoundForm(instance=player_round[0])
    return render(request, r'..\templates\player\score_entry.html', {'form': form})


@login_required()
def enter_scores(request):
    form = PlayerRoundForm(data=request.POST)
    message = ""
    if form.is_valid():
        form.save()
        message = 'Loaded Successfully'
        form = PlayerRoundForm()
    return render(request, r'..\templates\player\score_entry.html', {'form': form, 'message': message})


@login_required()
def list_scores(request):
    weeks = Week.objects.all()
    message = 'Select a week to view scores'
    return render(request, r'..\templates\player\list_scores.html', {'message': message, 'weeks': weeks})


@login_required()
def edit_scores(request, week_id):
    player_rounds = PlayerRound.objects.filter(week=week_id)
    return render(request, r'..\templates\player\edit_scores.html', {'player_rounds': player_rounds})
