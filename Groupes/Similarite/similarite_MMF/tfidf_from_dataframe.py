"""
V.0 : utilisation du vectorizer TF-IDF de scikit-learn sur une dataframe pandas issue des prétraitements (cf. script de parcours)
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics

def faux_tokeniseur(qqch):
    """
    permet d'éviter les prétraitements de scikit
    """
    return qqch

test = [{'id': 'iris32', 'question': ['ceci', 'est', 'un', 'texte', 'déjà', 'tokénisé']}, {'id': 'iris20', 'question': ['plus', 'que', 'tokénisé', 'déjà', 'prétraité', 'et', 'lemmatisé']}, {'id': 'iris45', 'question': ['ceci', 'est', 'un', 'texte', 'prétraité']}]
test_dataframe = pd.DataFrame(test)
print("Format de la dataframe :\n{}".format(test_dataframe))

tfidf = TfidfVectorizer(analyzer='word',tokenizer=faux_tokeniseur,preprocessor=faux_tokeniseur,token_pattern=None)
tfidf.fit(test_dataframe.question)
print(tfidf.vocabulary_)

print(metrics.pairwise.cosine_similarity(tfidf.transform(test_dataframe.question),tfidf.transform([['ceci', 'est', 'un', 'lapin', 'déjà', 'prétraité']])))