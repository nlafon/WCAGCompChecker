
def getSite(websiteURL):
    return "THE CODE FOR A WEBSITE GIVEN"

def checkSite(websiteURL):
    webSourceCode = getSite(websiteURL)
    
    results = {
        'violations' : 0,
        'warnings' : 0,
        'url': websiteURL,
        'webSourceCode': webSourceCode,
        'webRenderCode': '',
        }
    
    return results
