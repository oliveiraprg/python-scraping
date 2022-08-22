from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError


html = urlopen('https://pythonscraping.com/pages/page3.html')

bs = BeautifulSoup(html.read(), 'html5lib')
if html == None:
    print('site could not be found')
else:
    for child in bs.find('table', {'id':'giftList'}).children:
        print(child)
        
    for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
        print(sibling)