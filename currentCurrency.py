import requests
from bs4 import BeautifulSoup

url = "https://www.doviz.com/"

response = requests.get(url)

content = response.content

soup = BeautifulSoup(content, "html.parser")


altin = ""
dolar = ""
euro = ""

for f in soup.find_all("a", {"href": "//altin.doviz.com/gram-altin"}):
    for y in f.find_all("span", {"class": "menu-row2"}):
        altin = y.text 

for f in soup.find_all("a", {"href": "//kur.doviz.com/serbest-piyasa/amerikan-dolari"}):
    for y in f.find_all("span", {"class": "menu-row2"}):
        dolar = y.text 

for f in soup.find_all("a", {"href": "//kur.doviz.com/serbest-piyasa/euro"}):
    for y in f.find_all("span", {"class": "menu-row2"}):
        euro = y.text 

print("Altın:", altin)
print("Dolar:", dolar)
print("Euro:", euro)