"""
V.1 : utilisation du vectorizer TF-IDF de scikit-learn sur une dataframe pandas issue des prétraitements (cf. script de parcours)
comparaison de similarités
à ajouter : prétraitements de question, + d'infos dans la dataframe
"""

import numpy as np
import scipy
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics

def faux_tokeniseur(qqch):
    """
    permet d'éviter les prétraitements de scikit
    """
    return qqch

test = [{'id': 'iris32', 'question': ['ceci', 'est', 'un', 'texte', 'déjà', 'tokénisé']}, {'id': 'iris20', 'question': ['plus', 'que', 'tokénisé', 'déjà', 'prétraité', 'et', 'lemmatisé']}, {'id': 'iris45', 'question': ['ceci', 'est', 'un', 'texte', 'prétraité']}, {'id':'iris978', 'question':['demain','dès','l','aube']}, {'id':'iris7680', 'question':['à','l','heure','où','blanchit','la','campagne']}]
test_dataframe = pd.DataFrame(test)
print("Format de la dataframe :\n{}".format(test_dataframe))

tfidf = TfidfVectorizer(analyzer='word',tokenizer=faux_tokeniseur,preprocessor=faux_tokeniseur,token_pattern=None)
tfidf.fit(test_dataframe.question)
# print(tfidf.vocabulary_)

question = ['demain', 'est', 'un', 'texte', 'prétraité']
nb_questions = 3
# question = input("Posez une question : ")
simCosine = metrics.pairwise.cosine_distances(tfidf.transform(test_dataframe.question),tfidf.transform([question]))

for sim in sorted(list(simCosine), reverse=False)[:nb_questions]:
    print("Distance : {}, Question : {}".format(sim[0], test_dataframe.question[list(simCosine).index(sim)]))

print("*"*70)

simEuclidean = metrics.pairwise.euclidean_distances(tfidf.transform(test_dataframe.question),tfidf.transform([question]))

for sim in sorted(list(simEuclidean), reverse=False)[:nb_questions]:
    print("Distance : {}, Question : {}".format(sim[0], test_dataframe.question[list(simEuclidean).index(sim)]))

print("*"*70)

simManhattan = metrics.pairwise.manhattan_distances(tfidf.transform(test_dataframe.question),tfidf.transform([question]))

for sim in sorted(list(simManhattan), reverse=False)[:nb_questions]:
    print("Distance : {}, Question : {}".format(sim[0], test_dataframe.question[list(simManhattan).index(sim)]))