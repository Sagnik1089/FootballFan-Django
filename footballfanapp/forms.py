from django.forms import ModelForm
from .models import footballclub

class FootballClubForm(ModelForm):
    class Meta:
        model = footballclub
        fields = ['name','logo','official_site','home_venue','slogan','estd','country','league','abb','current_manager','manager_pic','description']