from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://cuiqingcai.com/990.html")
bsObj = BeautifulSoup(html, "html.parser")
link_list = bsObj.find_all(True)
for link in link_list:
    print(link.name)
# print(link_list)