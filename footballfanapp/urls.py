from django.urls import path
from . import views


urlpatterns = [
    path('name/<str:name>/<str:age>/',views.name, name='name'),
    path('',views.clubs, name='clubs'),
    path('club/<str:pk>/', views.club, name='club'),
    path('create-club/',views.createfootaballclub, name='create-club'),
    path('update-club/<str:pk>/', views.updatefootaballclub, name='update-club'), 
    path('delete-club/<str:pk>/',views.deletefootballclub,name='delete-club'), 
]
