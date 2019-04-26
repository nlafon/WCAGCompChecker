from django.shortcuts import render

from .models import URLForm
from utils.compliance_checker import checkSite

def resultView(request, standing):

    context = standing
    
    return render(request, 'resultsTest.html', context)

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
            
            # TODO: look further into why
            # Converts to string because jinja won't convert and render for some reason ¯\_(ツ)_/¯
            siteStanding['alt_text_violations'] = [alt_text_violation.__str__ for alt_text_violation in siteStanding['alt_text_violations']]

            return resultView(request, siteStanding)

    
    context['form'] = URLForm() 
        
    return render(request, 'homeTest.html', context)
