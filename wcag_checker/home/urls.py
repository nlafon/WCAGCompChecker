from django.urls import path

from . import views


urlpatterns = [
    path('', views.requestView, name='home'),
]
