# Bazinis scraping projektas

Šis projektas skirtas baziniam interneto svetainės scrapinimui, kuriame nurodomas svetainės https adresaas ir straipsnių vieta, iš kurios bus scrapinama

## Prieš pradedant

Turėtumėte įsitikinti, kad įrašytas BeautifulSoup https://pypi.org/project/beautifulsoup4/ 

## Failai
- 'scraper.py' - pagrindinis scraperis, jei svetainėje naudojamas div elementas. 
- 'scraper_h3.py' - papildomas scraperis, jei svetainėje naudojamas h3 elementas.
- 'main.py' - failas, kuris turės būti paleistas Jūsų terminale. Šiame faile taip pat rasite svetainių ir jų straipsnių div pavyzdžių. Pastaba: jei naudosite h3, turėsite pakoreguoti ir main.py

## Naudojimas

Įsirašykite beautifulsoup4
```bash
pip install requests beautifulsoup4

Paleiskite 'main.py' failą
```bash python main.py

Pastaba, jei naudojate python3, turėtų būti
```bash python3 main.py

Sistema paprašys įvesti html, pavyzdys:
```bash https://edition.cnn.com/

Tada spauskite enter ir įveskite elementą (atsiminkite, kas rašyta pradžioje dėl div ir h3)
```bash container__text container_lead-plus-headlines__text

Savo terminale matysite visą sąrašą straipsnių pavadinimų išrykiuotų pagal abecėlę

Gero naudojimo!