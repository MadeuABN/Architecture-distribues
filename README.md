# Architecture-distribues

Groupe 12 : Madavane - Philippe - Aroune

Sujet : Mettre en relation l'API Reddit sur un sujet Heathstone avec un site regroupant des données sur les decks Heathstones et les cartes qui les composent (http://metastats.net/).

Problématiques : Le but de ce projet était de pouvoir répondre à deux problématiques différentes, avec chacunes reliant un site à l'autres dans les deux sens. Dans un premier lieux ce projet nous aurait permis de voir si le winrate d'une carte (qu'il soit bon ou mauvais pouvait influencer son taux de popularité. Dans un second temps ce projet nous aurait permis de voir si la popularité d'une carte sur reddit pouvait avoir une influence sur son nombre de parties. 


# API Reddit : discussion u/Hearthstone

Dans le fichier : Architecturedistribués2.zip
Nous avons récupéré les 500 derniers tweets en format csv. (fichier untitled1.ipynb)
Les producer et consumer ne fonctionnent pas.


# Scrap : Site metastats

Dans le fichier : HSscrap.rar
On scrap dans un premier temps les données concernants les decks. Dans un second on scrap les données concernants les cartes à l'aide des données récupérées avant. Pour finir on regroupe les cartes apparaissant dans un plusieurs decks afin d'avoir les stats de chaques cartes.


# Visualisation : PowerBI

Dans le pdf : HS_visu.pdf
Sur le premier graphique on peut voir le nombre de like par rapport au poste.
Les deux suivants permettent de comparer le nombre de parties au nombre de likes par deck.
Le dernier permet quand à lui de voir l'évolution du nombre de parties au fil du temps selon les 3 decks les plus likés.

# Conclusion

Suite à notre travail sur l pipeline où l'on récupère, stock et traite nos données, nous avons pu répondre visuellement à notre problématique à l'aide de graphique produit sur PowerBI.
