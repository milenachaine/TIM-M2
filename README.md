# TIM-M2

Dépôt pour les étudiants [TIM](http://www.er-tim.fr) M2

## Objectifs généraux

Fabriquer un chatbot dans le domaine du juridique, capable de :

- demander des reformulations / précisions sur des questions
- répondre à des questions
	- en apportant une réponse d'une base de connaissances
	- en fournissant des pointeurs des textes des loi
- passer la main à un conseiller humain lorsqu'il n'est pas en mesure de répondre

## Tâches

- collecte d'un corpus de questions / réponses dans le juridique (forums, FAQ)
- prétraitement TAL du corpus, questions et réponses
	- lemmatisation
	- morpho-syntaxe / syntaxe
	- entités nommées
	- (intentions / entités)
	- (repérage de références juridiques)
- catégorisation des questions / réponses (sous-domaines du droit)
- modules d'interaction
	- traitement de la question (cf prétraitements)
	- recherche de réponses et/ou textes de loi par similarité
	- génération de réponses
