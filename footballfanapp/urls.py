from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('clubs/',views.clubs, name='clubs'),
    path('club/<str:pk>/', views.club, name='club'),
    path('create-club/',views.createfootaballclub, name='create-club'),
    path('update-club/<str:pk>/', views.updatefootaballclub, name='update-club'), 
    path('delete-club/<str:pk>/',views.deletefootballclub,name='delete-club'), 
    path('clubs/search/', views.search_clubs, name='search-clubs'), 
    path('clubs/filter/', views.filter_clubs, name='filter-clubs'), 
    path('clubs/sorted/', views.sort_clubs, name='sort-clubs'), 



    

    path('int-teams/',views.int_teams, name='int_teams'),
    path('int-team/<str:pk>/', views.int_team, name='int_team'),
    path('create-int-team/',views.createintteam, name='create-int-team'),
    path('update-int-team/<str:pk>/', views.updateintteam, name='update-int-team'),
    path('delete-int-team/<str:pk>/',views.deleteintteam,name='delete-int-team'),
    path('/int-teams/search/', views.search_int_teams, name='search-int-teams'), 
    path('/int-teams/continent/search/', views.filter_int_teams, name='filter-int-teams'), 
    path('/teams/sorted/',views.sort_int_teams, name='sort-int-teams')

    
]
