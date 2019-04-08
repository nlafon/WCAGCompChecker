
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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
            abs_img_url = urljoin(url,img['src'])
            alt_text_violations.append((img,abs_img_url))
            violations += 1
    # in case we want to display marked up versions
    marked_up_alt_text_violations = []
    for img in soup.find_all('img'):
        if not img.find('alt'):
            abs_img_url = urljoin(url,img['src'])
            img['src'] = abs_img_url
            img['style'] = 'border: 5px solid red;' # mark it up in soup
            marked_up_alt_text_violations.append(img)

    # TODO: find other violations...

    results = {
        'violations' : violations,
        'warnings' : warnings,
        'url': url,
        'soup': soup, # this will have injected styling but may look bad!
        'alt_text_violations': alt_text_violations,
        'marked_up_alt_text_violations': marked_up_alt_text_violations,
        'webRenderCode': '',
        }
    
    return results

if __name__ == '__main__':
    results = checkSite('https://johnalberse.com/sketchbook.html')
    print('url: ' + str(results['url']))
    print("Violations: " + str(results['violations']))
    print("Warnings: " + str(results['warnings']))
    print("No alt text in elements: ")
    for e in results['marked_up_alt_text_violations']:
        print(e)