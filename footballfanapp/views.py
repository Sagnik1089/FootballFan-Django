from django.shortcuts import render, redirect
from .models import footballclub,internationalteam
from .forms import FootballClubForm, InternationalForm
from django.core.paginator import Paginator


def home(request):
    return render(request, 'footballfanapp/home.html')


# Club Part

def clubs(request):
    all_clubs=footballclub.objects.all()
    paginator=Paginator(all_clubs,4)
    page = request.GET.get('page')
    clubs = paginator.get_page(page)
    mode=0
    return render(request, 'footballfanapp/clubs.html', {'clubs':clubs,'mode':mode})

def club(request,pk):
    club=footballclub.objects.get(id=pk)
    return render(request, 'footballfanapp/club.html', {'club':club})

def createfootaballclub(request):
    form=FootballClubForm()
    if request.method == 'POST':
        form=FootballClubForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clubs')
    return render(request, 'footballfanapp/footballclub_form.html',{'form':form})

def updatefootaballclub(request,pk):
    club=footballclub.objects.get(id=pk)
    form=FootballClubForm(instance=club)
    if request.method == 'POST': 
        form=FootballClubForm(request.POST, request.FILES, instance=club)
        if form.is_valid():
            form.save()
            return redirect('clubs')
    context={'form': form}
    return render(request, 'footballfanapp/footballclub_form.html',context)

def deletefootballclub(request,pk):
    club=footballclub.objects.get(id=pk)
    if request.method=='POST':
        club.delete()
        return redirect('clubs')
    context={'club': club}
    return render(request, 'footballfanapp/delete_club.html', context)

def search_clubs(request):
    query = request.GET.get('q', '')
    all_clubs = footballclub.objects.filter(name__icontains=query)
    paginator=Paginator(all_clubs,4)
    page = request.GET.get('page')
    clubs = paginator.get_page(page)
    mode=1
    return render(request, 'footballfanapp/clubs.html', {'clubs': clubs, 'mode':mode})

def filter_clubs(request):
    query_country = request.GET.get('q', '')
    query_ucl=request.GET.get('u','')
    if query_ucl=='':query_ucl=0        
    all_clubs = footballclub.objects.filter(country__icontains=query_country, ucl_won__gte=query_ucl)
    paginator=Paginator(all_clubs,4)
    page = request.GET.get('page')
    clubs = paginator.get_page(page)
    mode=1
    return render(request, 'footballfanapp/clubs.html', {'clubs': clubs,'mode':mode})

# End of Club Part

# International Part

def int_teams(request):
    all_teams=internationalteam.objects.all()
    paginator=Paginator(all_teams,4)
    page = request.GET.get('page')
    intTeamsObjs = paginator.get_page(page)
    mode=0
    return render(request, 'footballfanapp/int_teams.html', {'int_teams':intTeamsObjs,'mode':mode})

def int_team(request,pk):
    int_team=internationalteam.objects.get(id=pk)
    return render(request, 'footballfanapp/int_team.html', {'int_team':int_team})

def createintteam(request):
    form=InternationalForm()
    if request.method == 'POST':
        form=InternationalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('int_teams')
    return render(request, 'footballfanapp/int_team_form.html',{'form':form})

def updateintteam(request,pk):
    team=internationalteam.objects.get(id=pk)
    form=InternationalForm(instance=team)
    if request.method == 'POST': 
        form=InternationalForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect('int_teams')
    context={'form': form}
    return render(request, 'footballfanapp/int_team_form.html',context)

def deleteintteam(request,pk):
    team=internationalteam.objects.get(id=pk)
    if request.method=='POST':
        team.delete()
        return redirect('int_teams')
    context={'int_team': team}
    return render(request, 'footballfanapp/delete_int_team.html', context)

def search_int_teams(request):
    query = request.GET.get('q', '')
    all_int_teams = internationalteam.objects.filter(name__icontains=query)
    paginator=Paginator(all_int_teams,4)
    page = request.GET.get('page')
    int_teams = paginator.get_page(page)
    mode=1
    return render(request, 'footballfanapp/int_teams.html', {'int_teams': int_teams,'mode':mode})

def filter_int_teams(request):
    query_continent = request.GET.get('q', '')
    query_wc=request.GET.get('wc', '')
    if query_wc=='':query_wc=0 
    all_int_teams = internationalteam.objects.filter(continent__icontains=query_continent, wc_won__gte=query_wc)
    paginator=Paginator(all_int_teams,4)
    page = request.GET.get('page')
    int_teams = paginator.get_page(page)
    mode=1
    return render(request, 'footballfanapp/int_teams.html', {'int_teams': int_teams,'mode':mode})

# End of International Part