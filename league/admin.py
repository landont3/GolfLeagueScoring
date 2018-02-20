from django.contrib import admin

from .models import League, Division, Season, SeasonSettings, Course, Nine, Hole


@admin.register(SeasonSettings)
class SeasonSettingsAdmin(admin.ModelAdmin):
    list_display = ('season', 'handicap_method', 'max_score_to_par', 'max_handicap')
    list_editable = ('handicap_method', 'max_score_to_par', 'max_handicap')


admin.site.register(League)
admin.site.register(Division)
admin.site.register(Season)
admin.site.register(Course)
admin.site.register(Nine)
admin.site.register(Hole)
