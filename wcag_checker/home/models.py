from django.db import models
from django import forms

class checkRequest(models.Model):
    url = models.CharField(max_length=700)

    def __str__(self):
        return self.url

    def getForm():
        # This function is meant to return the form to be rendered for this model.
        
        return ""


class URLForm(forms.Form):
    url = forms.CharField(label='Website to check', max_length=3000)
