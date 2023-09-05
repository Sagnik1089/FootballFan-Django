from django.forms import ModelForm
from .models import footballclub

class FootballClubForm(ModelForm):
    class Meta:
        model = footballclub
        fields = ['name','abb','logo','description','estd','country']