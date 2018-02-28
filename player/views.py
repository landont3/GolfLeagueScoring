from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def welcome(request):
    return render(request, r'..\templates\player\welcome.html')


def player(request):
    return render(request, r'..\templates\player\score_entry.html')


