from django.shortcuts import render, redirect
from .models import footballclub,internationalteam
from .forms import FootballClubForm, InternationalForm


def home(request):
    return render(request, 'footballfanapp/home.html')


# Club Part
def clubs(request):
    clubObjs=footballclub.objects.all()
    return render(request, 'footballfanapp/clubs.html', {'clubs':clubObjs})

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
# End of Club Part

# International Part
def int_teams(request):
    intTeamsObjs=internationalteam.objects.all()
    return render(request, 'footballfanapp/int_teams.html', {'int_teams':intTeamsObjs})
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

# End of International Part