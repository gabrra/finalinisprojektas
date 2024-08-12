

#importuojam requests #daugiau apie requests cia: https://requests.readthedocs.io/en/latest/
import requests
from bs4 import BeautifulSoup

#pagrindine funkcija
def main():
    url = "https://x.com/search?q=supply%20chain%20management&src=typed_query" #isidedam nuoroda
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="css-175oi2r r-1f2l425 r-13qz1uu r-417010 r-18u37iz") #prie class_ reikalingas apatinis bruksnys, nes tai pythone naudojamas zodis

    print(f"Elements: {len(elements)}") #len yra length/ elementu kiekis
    
    
    
    # print(f"Skreipinam: {url}")
    # print(response) #response [200] - 200 reiskia statuso koda
    # print(response.content) #duoda visa html terminale, kad visa bardakeli susitvarkyti reikia kitos bibliotekos "beautiful soup"
    # #cia daugiau info apie beautiful soup https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    # #terminale irasome pip install beautifulsoup4

#jei vardas reiskia
if __name__ == "__main__":
    main()

#instaliuojames biblioteka su pip install requests
