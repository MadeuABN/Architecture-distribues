import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.common.exceptions import NoSuchElementException


df_decks = pd.read_csv('hsdecks.csv')

s = Service('C:/Users/Philippe/Documents/chromedriver_win32/chromedriver')
browser = webdriver.Chrome(service=s)


tailled = df_decks.shape[0]-1
#tailled = 10
ListeDF = []

for deck in range (0,tailled+1):
    print(deck)
    code = df_decks.iloc[deck]['Code']
    #Ouverture du site
    browser.get(f'http://metastats.net/hearthstone/deck/{str(code)}/')
    time.sleep(3)

    #Plein écran 
    browser.maximize_window()
    time.sleep(2)

    taille = 30
    ListeCards = []
    stop = 0

    #choisir deck
    for carte in range (1,taille+1):
        #récup info
        try:
            cost = browser.find_element(By.XPATH, f'//*[@id="page-wrapper"]/div/div[3]/div[1]/div/div/ul/li[{str(carte)}]/div[2]')
        except NoSuchElementException:
            stop = 1
            #break
        if (stop == 1):
            break
        nom = browser.find_element(By.XPATH, f'//*[@id="page-wrapper"]/div/div[3]/div[1]/div/div/ul/li[{str(carte)}]/div[3]/div/a')
        nbrcards = browser.find_element(By.XPATH, f'//*[@id="page-wrapper"]/div/div[3]/div[1]/div/div/ul/li[{str(carte)}]/div[4]')
        winrate = df_decks.iloc[deck]['Taux de victoire']
        nbrgames = df_decks.iloc[deck]['Nombre de parties']
        date = df_decks.iloc[deck]['Date']
        ListeCards.append(str(cost.text))
        ListeCards.append(str(nom.text))
        ListeCards.append(str(nbrcards.text))
        ListeCards.append(winrate)
        ListeCards.append(nbrgames)
        ListeCards.append(date)
        ListeDF.append(ListeCards[:])
        ListeCards.clear()
        #print(cost.text,nom.text,nbrcards.text,winrate,nbrgames,date)
    
#placer les infos dans un dataframe
df = pd.DataFrame(ListeDF)
df.columns = ['Coût', 'Nom', 'Quantité', 'Taux de victoire', 'Nombre de parties', 'Date']
df['Quantité'] = df['Quantité'].str[1:]
df.to_csv("hscards.csv")