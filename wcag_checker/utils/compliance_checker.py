
import requests
from bs4 import BeautifulSoup

def checkSite(url):
    '''
    Parses the html of the given URL to find usability
    issues. 

    Returns a dict with url, violation/warning counts, 
    and tags with violations. 

    The dict also contains a marked up BeautifulSoup object,
    (ie violations have a border around them), but this 
    doesn't play well with styling etc. 
    '''

    # get html from site and place in soup ds
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    
    # Warnings and violations cnt
    warnings = 0
    violations = 0

    # Find alt text violations in img tags
    alt_text_violations = []
    for img in soup.find_all('img'):
        if not img.find('alt'):
            img['style'] = 'border: 5px solid red;' # mark it up in soup
            alt_text_violations.append(img)
            violations += 1

    # TODO: find other violations...

    results = {
        'violations' : violations,
        'warnings' : warnings,
        'url': url,
        'soup': soup, # this will have injected styling but may look bad!
        'alt_text_violations': alt_text_violations,
        'webRenderCode': '',
        }
    
    return results

if __name__ == '__main__':
    results = checkSite('http://www.cs.ou.edu/~cgrant/')
    print('url: ' + str(results['url']))
    print("Violations: " + str(results['violations']))
    print("Warnings: " + str(results['warnings']))
    print("No alt text in elements: ")
    for e in results['alt_text_violations']:
        print(e)