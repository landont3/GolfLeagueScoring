from django.forms import ModelForm

from .models import PlayerRound


class RoundInput(ModelForm):
    class Meta:
        model = PlayerRound
        exclude = ('id',)
