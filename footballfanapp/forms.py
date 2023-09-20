from django.forms import ModelForm
from .models import footballclub

class FootballClubForm(ModelForm):
    class Meta:
        model = footballclub
        fields = ['name','logo','official_site','slogan','estd','country','league','abb','description']