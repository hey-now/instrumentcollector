from django.forms import ModelForm
from .models import Played

class PlayedForm(ModelForm):
    class Meta:
        model = Played
        fields = ['date', 'played']