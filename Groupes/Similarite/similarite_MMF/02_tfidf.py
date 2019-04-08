"""
V.2 : splitter tfidfdataframe.py en deux scripts, un qui calcule les poids tf-idf et un qui gère la recherche de similarités
utilisation du vectorizer TF-IDF de scikit-learn sur une dataframe pandas issue des prétraitements (cf. script de parcours)
"""
import warnings

warnings.filterwarnings("ignore")

import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def faux_tokeniseur(qqch):
    """
    permet d'éviter les prétraitements de scikit
    """
    return qqch


# on récupère le corpus prétraité (cf. script de parcours)
corpus = pd.read_pickle("./corpuspd.pkl")

print("Format de la dataframe :\n{}".format(corpus.head()))

# poids TF-IDF
tfidf = TfidfVectorizer(analyzer='word',tokenizer=faux_tokeniseur,preprocessor=faux_tokeniseur,token_pattern=None)
pickle.dump(tfidf.fit(corpus.lemmes), open("tfidf.pkl", "wb"))
print("Vocabulaire TF-IDF :\n{}".format(tfidf.vocabulary_))

