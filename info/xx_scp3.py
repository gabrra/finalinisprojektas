from bs4 import BeautifulSoup
import requests

url = "https://www.delfi.lt"

source = requests.get(url).text

soup = BeautifulSoup(source, 'html.parser')
blocks = soup.find_all('div', class_ = 'block-type-102-headline__title')

all_articles = []

for block in blocks:
    href = block.find("a")["href"]
    if href.startswith(url):
        all_articles.append(href)
    else:
        all_articles.append(url + href)

print(all_articles)


for article in all_articles:
    
    with open(f'naujienos/{article.rsplit("/", 1)[-1]}.txt', 'w') as f:
        source = requests.get(article).text
        soup = BeautifulSoup(source, 'html.parser')
        blocks = soup.find_all('div', class_="fragment fragment-html fragment-html--paragraph")
        for block in blocks:
            f.write(block.find("p").get_text() + '\n')