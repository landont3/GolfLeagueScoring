from django.forms import ModelForm

from .models import Week


class WeekForm(ModelForm):
    class Meta:
        model = Week
        exclude = []
