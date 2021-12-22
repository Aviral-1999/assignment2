import requests
from bs4 import BeautifullSoup4

req = requests.get("https://en.wikipedia.org/wiki/A")

soup = BeautifullSoup(req,'html')

summ = soup.find_all('div', class_="mw-parser-output)

l==17
for l in range(17,50):
    print(summ.select("p:nth-of-type("+str(l)+")"))



