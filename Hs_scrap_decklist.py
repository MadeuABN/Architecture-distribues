import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


s = Service('C:/Users/Philippe/Documents/chromedriver_win32/chromedriver')
browser = webdriver.Chrome(service=s)

#Ouverture du site
browser.get('http://metastats.net/hearthstone/decks/winrate/')
time.sleep(3)

#Plein écran 
browser.maximize_window()
time.sleep(2)

taille = 15
taille2 = 10
stop = 0
ListeDF = []
ListeDecks = []

for pages in range (1,taille2+1):
    if (stop == 1):
        break
    #changer page
    if (pages>1):
        nextpage = browser.find_element(By.XPATH, '//*[@id="deck-win-rates_next"]/a')
        nextpage.click()
        time.sleep(2)
    print(pages)
    #choisir deck
    for deck in range (1,taille+1):
        #récup info
        try:
            rank = browser.find_element(By.XPATH, f'//*[@id="deck-win-rates"]/tbody/tr[{str(deck)}]/td[1]')
        except NoSuchElementException:
            stop = 1
            #break
        if (stop == 1):
            break    
        nom = browser.find_element(By.XPATH, f'//*[@id="deck-win-rates"]/tbody/tr[{str(deck)}]/td[2]')
        nbrgames = browser.find_element(By.XPATH, f'//*[@id="deck-win-rates"]/tbody/tr[{str(deck)}]/td[3]')
        winrate = browser.find_element(By.XPATH, f'//*[@id="deck-win-rates"]/tbody/tr[{str(deck)}]/td[4]')
        ListeDecks.append(str(rank.text))
        ListeDecks.append(str(nom.text))
        ListeDecks.append(str(nbrgames.text))
        ListeDecks.append(str(winrate.text))
        ListeDF.append(ListeDecks[:])
        ListeDecks.clear()
        #print(rank.text,nom.text,nbrgames.text,winrate.text)
    
#placer les infos dans un dataframe
df = pd.DataFrame(ListeDF)
#adddate = []
date = browser.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/small')
date_text = date.text
df['dateact'] = date_text
df['dateact'] = df['dateact'].str.replace(r'^\D+', '', regex=True)
df['dateact'] = df['dateact'].str.slice(stop=-11)
df.columns = ['Rang', 'Nom', 'Nombre de parties', 'Taux de victoire' ,'Date']
df['Taux de victoire'] = df['Taux de victoire'].str.slice(stop=-1)
#df['Taux de victoire'] = df['Taux de victoire'].astype(float)
#df['Nombre de parties'] = df['Nombre de parties'].astype(int)
df[['Nom', 'Code']] = df['Nom'].str.split('#', expand=True)
df.to_csv("hsdecks.csv")