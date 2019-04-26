#from django.db import models
from django import forms

class URLForm(forms.Form):
    url = forms.CharField(label='', max_length=3000, widget=forms.TextInput(attrs={'class': "form-control shadow-sm"}))
