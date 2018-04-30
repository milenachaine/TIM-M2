#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Jielei Li - Mingqiang Wang - Arthur Provenier

    Création du tf-idf sur l'ensemble des documents
    Retourn : les 30 premiers mots avec le score le plus élevé
"""

from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from lxml import etree

def get_tfidf(fichier):
    with open(fichier, 'r') as f:
        tree = etree.parse(f)

    textes = [texte.text for texte in tree.xpath('//text')]

    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()

    tfidf = transformer.fit_transform(vectorizer.fit_transform(textes))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()

    dict_tfidf = {}
    for i in range(0, len(weight)):
        for j in range(0, len(word)):
            if not weight[i][j] == 0:
                dict_tfidf[weight[i][j]] = word[j]

    values = sorted(dict_tfidf.keys(), reverse=True)[:30]
    features = [dict_tfidf[v] for v in values if not dict_tfidf[v] == 'de']

    return set(features)
