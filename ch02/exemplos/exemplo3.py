from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError


html = urlopen('https://pythonscraping.com/pages/page3.html')

bs = BeautifulSoup(html.read(), 'html5lib')
print(bs.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
