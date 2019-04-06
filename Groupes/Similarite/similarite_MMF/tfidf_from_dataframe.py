"""
V.1 : utilisation du vectorizer TF-IDF de scikit-learn sur une dataframe pandas issue des prétraitements (cf. script de parcours)
comparaison de similarités
la question est prétraitée avec treetagger, cf. phrase2conll.py
"""

import pandas as pd
import phrase2conll
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics

def faux_tokeniseur(qqch):
    """
    permet d'éviter les prétraitements de scikit
    """
    return qqch

transition = "*"*50

corpus = pd.read_pickle("./corpuspd.pkl")

print("Format de la dataframe :\n{}".format(corpus))

tfidf = TfidfVectorizer(analyzer='word',tokenizer=faux_tokeniseur,preprocessor=faux_tokeniseur,token_pattern=None)
tfidf.fit(corpus.lemmes)
# print(tfidf.vocabulary_)

question = input("Posez une question : ")
q_lemmes = []
for l in phrase2conll.main(question).rstrip().split(' '):
    q_lemmes.append(l.split("/")[2])

print("Question lemmatisée : ", q_lemmes)

nb_questions = int(input("Sélectionner combien de réponses ? (entre 1 et 10) "))
assert 0 < nb_questions < 11, "ENTRE 1 ET 10"

print(transition, "COSINE", transition)

simCosine = metrics.pairwise.cosine_distances(tfidf.transform(corpus.lemmes),tfidf.transform([q_lemmes]))

for sim in sorted(list(simCosine), reverse=False)[:nb_questions]:
    q_sim = ' '.join(corpus.mots[list(simCosine).index(sim)])
    print("Distance : {}, Question : {}".format(sim[0], q_sim))

print(transition, "EUCLIDEAN", transition)

simEuclidean = metrics.pairwise.euclidean_distances(tfidf.transform(corpus.lemmes),tfidf.transform([q_lemmes]))

for sim in sorted(list(simEuclidean), reverse=False)[:nb_questions]:
    q_sim = ' '.join(corpus.mots[list(simEuclidean).index(sim)])
    print("Distance : {}, Question : {}".format(sim[0], q_sim))

print(transition, "MANHATTAN", transition)

simManhattan = metrics.pairwise.manhattan_distances(tfidf.transform(corpus.lemmes),tfidf.transform([q_lemmes]))

for sim in sorted(list(simManhattan), reverse=False)[:nb_questions]:
    q_sim = ' '.join(corpus.mots[list(simManhattan).index(sim)])
    print("Distance : {}, Question : {}".format(sim[0], q_sim))