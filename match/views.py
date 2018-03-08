from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Week, Match


@login_required()
def welcome(request):
    return render(request, r'..\templates\match\welcome.html')


@login_required()
def week_list(request):
    weeks = Week.objects.all()
    return render(request, r'..\templates\match\week_list.html', {'weeks': weeks})


@login_required()
def match_list(request, week_id):
    matches = Match.objects.filter(week=week_id)
    week = Week.objects.filter(id=week_id)
    return render(request, r'..\templates\match\match_list.html', {'matches': matches, 'week': week[0]})


@login_required()
def match_edit(request, match_id):
    match = Match.objects.filter(id=match_id)
    return render(request, r'..\templates\match\match_edit.html', {'match': match[0]})
