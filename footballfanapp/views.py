from django.shortcuts import render, redirect
from .models import footballclub
from .forms import FootballClubForm

def name(request,name,age):
    context={'name': name, 'age': int(age)}
    return render(request, 'footballfanapp/name.html',context)

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