# Catégorisation des questions / réponses

## 1. Info du groupe : 
### Membres : Chunyang JIANG, Yizhou XU

## 2. Données
### Entrée : 
### Sortie : 

## 3. Recherche documentaire : les branches du droit en France

(Provisoire, à préciser)

+ Les subdivisions du droit public

    1. Droit constitutionnel
    2. Droit administratif
    3. Droit des finances publiques
    4. ~~Droit international public~~

+ Les subdivisions du droit privé
    1. le Droit civil
    2. le Droit commercial
    3. le Droit social
    4. ~~le Droit international privé~~

## 4. Travail réalisé
(MAJ 19/02/2019)
* Entraînement d'un modèle
    * Modèle : [tfidf_rf_clf](tfidf_rf_clf)
    * Script : [cat.py](cat.py)
    * Corpus d'entraînement : [80% du corpusIrisVersion3](../Crawling/corpusIrisVersion3.xml)
    * *Features* : 500 tfidf des mots avec les meilleurs scores
    * Classifier : [Ramdom Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
    * Paramétrage : [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
    * Evaluation : cf [eval.md](eval.md)
    * Test : un petit test avec un nouvel jeu de données, cf [test_model.py](test_model.py)

## 5. TODO
(MAJ 19/02/2019)
* Résélection de *features*
* Réechantillonnage du corpus d'entraînement
* Définition des classes
* Evaluation et comparaison de plusieurs classifieurs

## Références

+ http://medias.dunod.com/document/9782100774913/Feuilletage.pdf
+ https://baripedia.org/wiki/Les_diff%C3%A9rentes_branches_du_droit
+ http://www.cours-de-droit.net/les-principales-branches-du-droit-prive-et-du-droit-public-a121611802
+ https://fr.wikipedia.org/wiki/Branche_du_droit_en_France#Distinction_entre_droit_priv%C3%A9_et_droit_public
