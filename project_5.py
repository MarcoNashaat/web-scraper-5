#enabling https
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#importing libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#function to get external links
def get_external_links(url):
    links = []    

    #retriving the page and creating bs object
    html = urlopen(url)
    bs = BeautifulSoup(html,'html.parser')

    #getting all links that doesn't contain current url
    external_links = bs.find_all('a',href=re.compile('^(http|www)((?!'+url+').)*$'))

    #loop through found links and adding the appropriate
    for link in external_links:
        if link['href'] and link['href'] not in links:
            links.append(link['href'])
    return links

print(get_external_links('http://www.oreilly.com'))