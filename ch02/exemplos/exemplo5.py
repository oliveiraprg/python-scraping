from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('https://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html5lib')
len_tags = bs.find_all(lambda tag: len(tag.attrs) == 2)

print(len_tags)
