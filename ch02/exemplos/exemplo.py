from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html5lib')
        title = bs.body.h1
    except AttributeError as e:
        return None    
    return title


def getSpan(url, color):
    color = str(color)
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html5lib')
        nameList = bs.find_all('span', {'class':f'{color}'})
    except AttributeError as e:
        return None    
    return nameList


title = getTitle('https://pythonscraping.com/pages/warandpeace.html')
if title == None:
    print('Title could not be found')
else:
    print(title)

span_green = getSpan('https://pythonscraping.com/pages/warandpeace.html', 'green')
if span_green == None:
    print('tag could not be found')
else:
    for tag in span_green:
        print(tag.get_text())
