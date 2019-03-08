#from django.db import models
from django import forms

class URLForm(forms.Form):
    url = forms.CharField(label='Website to check', max_length=3000)
