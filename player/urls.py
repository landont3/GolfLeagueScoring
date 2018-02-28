from django.urls import path

from .views import player, welcome


urlpatterns = [
    path('', welcome, name='player_home'),
    path('entry/', player),
]
