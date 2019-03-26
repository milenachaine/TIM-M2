# Crawling

## Objectif et tâches

- Crawler plusieurs forums de droit afin de constituer un corpus de questions/réponses
- Créer un fichier XML facile à parser et reprenant des infos clé

![Test](/Images/web_crawler_logo.png)

## Forums crawlés

- NetIris (plus de 300K questions, 8 catégories)
- Juritravail (plus de 150K questions, 27 catégories)

[IMA Juritravail]

## Corpus et métadonnées

- Pour le calcul de similarité : une suite de questions-réponses plain text
- Pour la catégorisation : la catégorie de la question telle qu'indiqué sur le site
- D'autres métadonnées utiles :
	- un id unique par doc
	- le nom du site
	- le titre de la page
	- l'url de la page

[IMA XML]

## Filtrage des réponses

- Élimination des réponses "vides" en filtrant sur la popularité des auteurs

[IMA Juritravail]

## Technologie utilisée

- Python
- Bibliothèque BeautifulSoup

[Logo BeautifulSoup]

## Statistiques du corpus

NetIris : 41229 questions, 60421 réponses aspirées
Juritravail : 

[IMA graphiques]
