from django.forms import ModelForm
from .models import footballclub, internationalteam

class FootballClubForm(ModelForm):
    class Meta:
        model = footballclub
        fields = ['name','logo','official_site','home_venue','slogan','estd','country','league','abb','current_manager','manager_pic','ucl_won','description']

class InternationalForm(ModelForm):
    class Meta:
        model = internationalteam
        fields = ['name','logo','official_site','abb','current_manager','manager_pic','wc_won','copa_won','euro_won','description']