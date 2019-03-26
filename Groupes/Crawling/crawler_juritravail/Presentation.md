# Crawling

## Objectif et tâches

- Crawler plusieurs forums de droit afin de constituer un corpus de questions/réponses
- Créer un fichier XML facile à parser et reprenant des infos clé

![Crawler logo](/Groupes/Crawling/crawler_juritravail/Images/web_crawler_logo.png)

## Forums crawlés

- NetIris (plus de 300K questions, 8 catégories)
- Juritravail (plus de 150K questions, 27 catégories)

![Juritravail](/Groupes/Crawling/crawler_juritravail/Images/screenshot_juritravail.png)

## Corpus et métadonnées

- Pour le calcul de similarité : une suite de questions-réponses plain text
- Pour la catégorisation : la catégorie de la question telle qu'indiqué sur le site
- D'autres métadonnées utiles :
	- un id unique par doc
	- le nom du site
	- le titre de la page
	- l'url de la page

![XML](/Groupes/Crawling/crawler_juritravail/Images/screenshot_corpus_juritravail.png)

## Filtrage des réponses

- Élimination des réponses "vides" en filtrant sur la popularité des auteurs

![Réponse Juritravail](/Groupes/Crawling/crawler_juritravail/Images/screenshot_juritravail_reponse.png)

## Technologie utilisée

- Python
- Bibliothèque BeautifulSoup

![Logo BeautifulSoup](/Groupes/Crawling/crawler_juritravail/Images/BeautifulSoup.png)

## Statistiques du corpus

NetIris : 41229 questions, 60421 réponses aspirées
Juritravail : 126911 question, 75019 réponses aspirées

![Graphique_1](/Groupes/Crawling/crawler_juritravail/Images/categories_netiris.png)
![Graphique_2](/Groupes/Crawling/crawler_juritravail/Images/categories_juritravail.png)
