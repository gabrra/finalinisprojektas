from bs4 import BeautifulSoup #klase
import requests #biblioteka
import schedule 
import time 

# naudojama svetaine
url = "https://www.bbc.com"  


#paimamas tekstas is svetaines
source = requests.get(url).text
soup = BeautifulSoup(source, 'html.parser') #kuriamas naujas objektas, paduodamas html.parser kaip stringas - budas kaip parsinti

blocks = soup.find_all('div', class_='sc-4fedabc7-0 kZtaAl') #surandame bendra vardikli - pavadinima straipsniu

titles = [block.get_text(strip=True) for block in blocks] #norime pasiziureti kas gavosi
sorted_titles = sorted(titles) #norime surusiuoti straipsniu pavadinimus pagal abecele

for title in sorted_titles: 
    print(title) # norime pamatyti terminale kokie pavadinimai gauti 

