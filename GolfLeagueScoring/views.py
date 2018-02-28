from django.shortcuts import render, redirect


def welcome(request):
    if request.user.is_authenticated:
        return render(request, r'..\templates\welcome.html')
    else:
        return redirect('login')


def login(request):
    return render(request, r'..\templates\login.html')