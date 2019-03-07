from django.db import models

class checkRequest(models.Model):
    url = models.CharField(max_length=700)

    def __str__(self):
        return self.url

    def getForm():
        # This function is meant to return the form to be rendered for this model.
        return ""
