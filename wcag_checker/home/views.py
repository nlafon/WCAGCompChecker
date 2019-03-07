from django.shortcuts import render

from .models import checkRequest, URLForm
from utils.compliance_checker import checkSite

def requestView(request):

    context = {}

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = URLForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            print('Valid form')
            websiteURL = form.cleaned_data['url']

            print(websiteURL)
            siteStanding = checkSite(websiteURL)
            print(siteStanding)

            context['form'] = URLForm() 
            return render(request, 'home.html', context)

    else:
        context['form'] = URLForm() 
        
    return render(request, 'home.html', context)
