# Bazinis scraping projektas

Šis projektas skirtas baziniam interneto svetainės scrapinimui, kuriame nurodomas svetainės https adresas ir straipsnių vieta, iš kurios bus scrapinama

## Prieš pradedant

Turėtumėte įsitikinti, kad įrašytas BeautifulSoup https://pypi.org/project/beautifulsoup4/ 

## Failai
- 'scraper.py' - pagrindinis scraperis, jei svetainėje naudojamas div elementas
- 'main.py' - failas, kuris turės būti paleistas terminale. Šiame faile taip pat rasite svetainių ir jų straipsnių div pavyzdžių. 
## Naudojimas

Įsirašykite beautifulsoup4
```pip install requests beautifulsoup4```

Paleiskite 'main.py' failą
```python main.py```

Pastaba, jei naudojate python3, turėtų būti
```python3 main.py```

Sistema paprašys terminale pasirinkti vieno iš penkių siūlomų html numerį (1-5):
```Choose website to scrape:
1. BBC
2. CNN
3. Economist
4. LRT
5. 15min
```

Tada spauskite enter.

Savo terminale matysite visą sąrašą straipsnių pavadinimų išrykiuotų pagal abecėlę.

Gero naudojimo!
# CA-projektas
