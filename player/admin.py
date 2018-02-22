from django.contrib import admin

from .models import Person, Player, TeamPlayers


admin.site.register(Person)
admin.site.register(Player)
admin.site.register(TeamPlayers)
