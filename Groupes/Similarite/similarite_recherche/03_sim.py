"""
V.2 : splitter tfidfdataframe.py en deux scripts, un qui calcule les poids tf-idf et un qui gère la recherche de similarités
utilisation du vectorizer TF-IDF de scikit-learn sur une dataframe pandas issue des prétraitements (cf. script de parcours)
comparaison de similarités
la question est prétraitée avec treetagger, cf. phrase2conll.py
"""
import warnings

warnings.filterwarnings("ignore")

import pandas as pd
import pickle
import phrase2conll
from prettytable import PrettyTable
import glob
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics

def faux_tokeniseur(qqch):
    """
    permet d'éviter les prétraitements de scikit
    """
    return qqch

def generer_visu(mini_corpus):
    """
    contrôle visualisation des similarités
    """
    for i in mini_corpus.index:
        id = mini_corpus.loc[i, 'id']
        sim = mini_corpus.loc[i, 'simCosine']
        q = ' '.join(mini_corpus.loc[i, 'mots'])
        tab = PrettyTable(["ID", "DISTANCE"])
        tab.add_row([id, sim])
        print(tab)
        print("QUESTION : {}".format(q))

sep = "-"*70
message = "Usage : python3 {} <dataframe du corpus>".format(sys.argv[0])
if len(sys.argv) != 2:
	print(sep)
	print("Nombre d'arguments incorrect")
	print(message)
	print(sep)
	exit()
elif not glob.glob(sys.argv[1]):
	print(sep)
	print("{} est introuvable".format(sys.argv[1]))
	print(message)
	print(sep)
	exit()
else:
	print(sep)
	print("Ouverture de {} en cours".format(sys.argv[1]))
	print(sep)

corpuspd = sys.argv[1]
# on récupère le corpus prétraité (cf. script de parcours)
corpus = pd.read_pickle(corpuspd)
corpus = corpus.set_index(pd.Index(range(0,len(corpus))))

# cf. 02_tfidf.py
tfidf_fit = pickle.load(open("./tfidf_fit.pickle", "rb"))
tfidf_transform = pickle.load(open("./tfidf_transform.pickle","rb"))

question = input("Posez une question : ")
assert question, "Question vide"

# appel phrase2conll pour gérer question
q_lemmes = []
for l in phrase2conll.main(question).rstrip().split(' '):
    q_lemmes.append(l.split("/")[2])

print("Question lemmatisée : ", q_lemmes)

nb_questions = int(input("Nombre de réponses à sélectionner (entre 1 et 10) : "))
assert 0 < nb_questions < 11, "ENTRE 1 ET 10"

# calcul et comparaison des similarités
print(sep)
print("COSINUS")
print(sep)

simCosine = metrics.pairwise.cosine_distances(tfidf_transform,tfidf_fit.transform([q_lemmes]))
corpus['simCosine'] = simCosine
corpus = corpus.sort_values(by=['simCosine'])
repCosine = corpus[:nb_questions]
generer_visu(repCosine)

print(sep)
print("EUCLIDEAN")
print(sep)

simEuclidean = metrics.pairwise.euclidean_distances(tfidf_transform,tfidf_fit.transform([q_lemmes]))
corpus['simEuclidean'] = simEuclidean
corpus = corpus.sort_values(by=['simEuclidean'])
repEuclidean = corpus[:nb_questions]
generer_visu(repEuclidean)

# for sim in sorted(list(simEuclidean), reverse=False)[:nb_questions]:
#     generer_visu(simEuclidean, sim)
#
print(sep)
print("MANHATTAN")
print(sep)

simManhattan = metrics.pairwise.manhattan_distances(tfidf_transform,tfidf_fit.transform([q_lemmes]))
corpus['simManhattan'] = simManhattan
corpus = corpus.sort_values(by=['simManhattan'])
repManhattan = corpus[:nb_questions]
generer_visu(repManhattan)

# for sim in sorted(list(simManhattan), reverse=False)[:nb_questions]:
#     generer_visu(simManhattan, sim)

corpus.drop(columns=['simCosine', 'simEuclidean', 'simManhattan'])