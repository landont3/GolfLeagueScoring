from django.forms import ModelForm

from .models import PlayerRound


class PlayerRoundForm(ModelForm):
    class Meta:
        model = PlayerRound
        exclude = []