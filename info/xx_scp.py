from bs4 import BeautifulSoup #klase
import requests #biblioteka

url = "https://www.delfi.lt"

source = requests.get(url).text #su requests biblioteka panaudojama get funkcija
# # skliaustuose nurodoma svetaine is kurios scrapinama
# # taip pat nurodoma kokio formato norima, t.y. text
# # print(source[:5000]) # <--- su situo atsiprintinam pirmus 5000 dalyku
# # pacioje svetaineje paspaudus fn ir f12 pamatysime html koda, jame reikia rasti bendra vardikli, kas slepiasi ko elementu
# # bendri vardikliai tiketina, kad bus aprasyti kazkokiomis klasemis
# # po klase slepasi visa informacija, kuri domina

# soup = BeautifulSoup(source, 'html.parser') #kuriamas naujas objektas, paduodamas html.parser kaip stringas - budas kaip parsinti
# blokas = soup.find('div', class_ = 'block-type-102-headline__title')
# # gavome sriubos objekta, kuriame yra visokiu metodu, pvz .find, kurie mums padeda issrinkti mus dominancius elementus
# # siuo atveju ieskome 'div' bloko, kuriame butu headline
# print(blokas.find("a").get_text()) #atsiprintiname kas yra tas headline

# # kaip paimti visus straipsnius - reikia susirasti bendra klase, kuria visi tekstai turi, kad galetume gauti sarasa dalyku
# soup = BeautifulSoup(source, 'html.parser') #kuriamas naujas objektas, paduodamas html.parser kaip stringas - budas kaip parsinti
# blocks = soup.find_all('div', class_ = 'block-type-102-headline__title')
# # gavome sriubos objekta, kuriame yra visokiu metodu, pvz .find, kurie mums padeda issrinkti mus dominancius elementus
# # siuo atveju ieskome 'div' bloko, kuriame butu headline
# for block in blocks:
#     print(block.find("a").get_text())

# # jei norime issitraukti ne tik pavadinimus, bet ir nuorodas
soup = BeautifulSoup(source, 'html.parser') #kuriamas naujas objektas, paduodamas html.parser kaip stringas - budas kaip parsinti
blocks = soup.find_all('div', class_ = 'block-type-102-headline__title') #surandame bendra vardikli
# # gavome sriubos objekta, kuriame yra visokiu metodu, pvz .find, kurie mums padeda issrinkti mus dominancius elementus
# # siuo atveju ieskome 'div' bloko, kuriame butu headline
# for block in blocks:
#     print(block.find("a")["href"])

all_articles = [] #tuscias listas

# # jei norime, kad mums suziuretu nuorodas:
for block in blocks:
    href = block.find("a")["href"]
    if href.startswith(url):
        all_articles.append(href)
    else:
        all_articles.append(url + href)

print(all_articles) #turesime sarase visu straipsniu

# # kaip issitraukti info is saraso:
# for article in all_articles:
#     source = requests.get(article).text #pasiimam source, url bus aticle
#     soup = BeautifulSoup(source, 'html.parser')  #sriuba bus su nauju source
#     # #tada ziurime po kuo slepiasi pats tekstas
#     print(f"reading article: {article}")
#     print()
#     blocks = soup.find_all('div', class_="fragment fragment-html fragment-html--paragraph") #paduodame kaip stringa
#     for block in blocks:
#         print(block.find("p").get_text())
#         input()

# # kaip issaugoti teksta faile:
for article in all_articles:

    with open(f'naujienos/{article.rsplit("/", 1)[-1]}.txt', 'w') as f: #atsidaro failiukas kuris vadinasi kaip straipsnio pavadinimas po slasho
        #viskas issaugoma su .txt, nurodome w mode - write ir sita faila f: naudosime kaip f raidele
        source = requests.get(article).text #pasiimam source, article is nuorodos
        soup = BeautifulSoup(source, 'html.parser')  #sriuba bus su nauju source 
        blocks = soup.find_all('div', class_="fragment fragment-html fragment-html--paragraph") #paduodame kaip stringa, sriuba suras visus div su siais fragmentais
        # po jais slepiasi paragrafai, kuriuos liepiame surasti 
        for block in blocks:
            f.write(block.find("p").get_text() + '\n') #ir kiekviena bloka irasyk #get_text nuima visus html dalykus, tagus ir paima gryna teksta
        # 'p' reiskia paragrafas
 
    # input() #kad sustotu irases viena straipsnis #jei isimsime sita, surinks viska

