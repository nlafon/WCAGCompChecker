from django.shortcuts import render

from .models import URLForm
from utils.compliance_checker import checkSite

def resultView(request, standing):

    context = standing
        
    return render(request, 'results.html', context)

def requestView(request):

    context = {}

    # Process form if it is a post
    if request.method == 'POST':

        # Create a form and populate it with the request data
        form = URLForm(request.POST)
        
        if form.is_valid():
            websiteURL = form.cleaned_data['url']

            print('Valid form')
            
            print(websiteURL)
            siteStanding = checkSite(websiteURL)
            print(siteStanding)

            #context['form'] = URLForm() 
            #return render(request, 'home.html', context)

            return resultView(request, siteStanding)

    
    context['form'] = URLForm() 
        
    return render(request, 'home.html', context)
