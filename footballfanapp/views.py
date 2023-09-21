from django.shortcuts import render, redirect
from .models import footballclub,internationalteam
from .forms import FootballClubForm, InternationalForm
from django.core.paginator import Paginator

crr_clubs=footballclub.objects.all()
crr_int_teams=footballclub.objects.all()

def home(request):
    return render(request, 'footballfanapp/home.html')


# Club Part

def clubs(request):
    global crr_clubs
    all_clubs=footballclub.objects.all().order_by('name')
    crr_clubs=all_clubs
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
    global crr_clubs
    query = request.GET.get('q', '')
    all_clubs = crr_clubs.filter(name__icontains=query)
    crr_clubs=all_clubs
    paginator=Paginator(all_clubs,4)
    page = request.GET.get('page')
    clubs = paginator.get_page(page)
    mode=1
    return render(request, 'footballfanapp/clubs.html', {'clubs': clubs, 'mode':mode})

def filter_clubs(request):
    global crr_clubs
    query_country = request.GET.get('q', '')
    query_ucl=request.GET.get('u','')
    if query_ucl=='':query_ucl=0        
    all_clubs = crr_clubs.filter(country__icontains=query_country, ucl_won__gte=query_ucl)
    crr_clubs=all_clubs
    paginator=Paginator(all_clubs,4)
    page = request.GET.get('page')
    clubs = paginator.get_page(page)
    mode=1
    return render(request, 'footballfanapp/clubs.html', {'clubs': clubs,'mode':mode})

# End of Club Part

# International Part

def int_teams(request):
    global crr_int_teams
    all_teams=internationalteam.objects.all().order_by('name')
    crr_int_teams=all_teams
    print(50*'*',type(all_teams),50*'*')
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
    global crr_int_teams
    query = request.GET.get('q', '')
    all_int_teams = crr_int_teams.filter(name__icontains=query)
    crr_int_teams=all_int_teams
    paginator=Paginator(all_int_teams,4)
    page = request.GET.get('page')
    int_teams = paginator.get_page(page)
    mode=1
    return render(request, 'footballfanapp/int_teams.html', {'int_teams': int_teams,'mode':mode})

def filter_int_teams(request):
    global crr_int_teams
    query_continent = request.GET.get('q', '')
    query_wc=request.GET.get('wc', '')
    if query_wc=='':query_wc=0 
    all_int_teams = crr_int_teams.filter(continent__icontains=query_continent, wc_won__gte=query_wc)
    crr_int_teams=all_int_teams
    paginator=Paginator(all_int_teams,4)
    page = request.GET.get('page')
    int_teams = paginator.get_page(page)
    mode=1
    return render(request, 'footballfanapp/int_teams.html', {'int_teams': int_teams,'mode':mode})

# End of International Part