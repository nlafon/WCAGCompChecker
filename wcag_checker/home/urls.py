from django.urls import path

from . import views


urlpatterns = [
    path('', views.requestView, name='home'),
    path('team', views.teamView, name='team'),
    
]
