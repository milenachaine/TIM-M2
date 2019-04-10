"""
à partir d'une dataframe pandas, on apprend le vocabulaire tf-idf (poids globaux)
on transforme le corpus à partir de ces poids
on transfert ces informations dans deux pickles
"""
import warnings

warnings.filterwarnings("ignore")

import pickle
import pandas as pd
import sys
import glob
from sklearn.feature_extraction.text import TfidfVectorizer


def faux_tokeniseur(qqch):
    """
    permet d'éviter les prétraitements de scikit
    """
    return qqch

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
	print("Traitement de {} en cours".format(sys.argv[1]))
	print(sep)

corpuspd = sys.argv[1]
# on récupère le corpus prétraité (cf. script de parcours)
corpus = pd.read_pickle(corpuspd)

print(sep)
print("Format de la dataframe :\n{}".format(corpus.head()))

# poids TF-IDF
tfidf = TfidfVectorizer(analyzer='word',tokenizer=faux_tokeniseur,preprocessor=faux_tokeniseur,token_pattern=None)
tfidf_fit = tfidf.fit(corpus.lemmes)
tfidf_transform = tfidf_fit.transform(corpus.lemmes)

print(sep)
print("Génération de tfidf_fit.pickle et tfidf_transform.pickle")
pickle.dump(tfidf_fit,open("tfidf_fit.pickle", "wb"))
pickle.dump(tfidf_transform, open("tfidf_transform.pickle", "wb"))

print(sep)
print("Vocabulaire TF-IDF :\n{}".format(tfidf_fit.vocabulary_))

