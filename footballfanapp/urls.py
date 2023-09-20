from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('clubs/',views.clubs, name='clubs'),
    path('club/<str:pk>/', views.club, name='club'),
    path('create-club/',views.createfootaballclub, name='create-club'),
    path('update-club/<str:pk>/', views.updatefootaballclub, name='update-club'), 
    path('delete-club/<str:pk>/',views.deletefootballclub,name='delete-club'), 
]
