from django.contrib import admin

from .models import Week, TeamHeader, Team, Match


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'week', 'first_team', 'second_team', 'starting_hole')
    list_editable = ('starting_hole',)


@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'number', 'nine', 'season', 'division')
    list_editable = ('nine',)


admin.site.register(TeamHeader)
admin.site.register(Team)
