from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html.read(), 'html5lib')

for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
