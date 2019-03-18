"""Classifier of legal textual documents.



"""
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys

import argparse
from argparse import RawTextHelpFormatter
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import ComplementNB
from sklearn.dummy import DummyClassifier

from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from pandas_ml import ConfusionMatrix

import spacy

from settings import *

CLF = {
    "rf": RandomForestClassifier,
    "svm": LinearSVC,
    "nb": ComplementNB,
    "dummy": DummyClassifier
}

def main():
    args = get_args()

    # prepare data
    X, Y = prepare_data(args.corpus, args.features)

    # train_test protocol: 8:2
    x_train, x_test, y_train, y_test = \
        train_test_split(X, Y, test_size=0.2, random_state=12)

    # build pipeline
    parameters = CLF_PARAM[args.classifier]
    clf = CLF[args.classifier](**parameters)
    vectorizer = TfidfVectorizer(max_features=FEATURE_SIZE)
    pipeline = Pipeline([
        ('tfidf', vectorizer),
        ('clf', clf)
    ])

    # experiment
    pipeline.fit(x_train, y_train)
    y_pred = pipeline.predict(x_test)

    # evaluation
    print(metrics.classification_report(y_test, y_pred))
    print(ConfusionMatrix(y_test, y_pred))

    # save model
    if args.output:
        joblib.dump(pipeline, args.output)

def get_args():
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument('corpus')
    parser.add_argument(
        '-c', "--classifier",
        choices=['rf', 'svm', 'nb', 'dummy'],
        default='dummy',
        help=CLF_HELP
    )
    parser.add_argument(
        '-f', "--features",
        choices=["token","lemma","ngram"],
        default="token",
        help=FEAT_HELP
    )
    parser.add_argument('-s', "--feature_size", default=FEATURE_SIZE)
    parser.add_argument('-o', "--output")
    return parser.parse_args()

def prepare_data(corpus,feat):
    tree = ET.ElementTree(file=corpus)
    X = list()
    Y = list()
    for doc in tree.getroot():
        question = " ".join([q.text.strip() for q in doc.findall("question")])
        Y.append(DOC_CLASS[doc.get("class").lower()])
        X.append(question)
    if feat == "lemma":
        nlp = spacy.load('fr', vectors=False)
        for i in range(X.__len__()):
            X[i] = " ".join([token.lemma_ for token in nlp(X[i])])
    return (X,Y)

def lemmatizer(text):
    import treetaggerwrapper
    result = []
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr')
    tags = tagger.tag_text(text)
    for token in tags:
        form,pos,lemme = token.split("\t")
        if lemme != "@card@":
            result.append(lemme)
        else:
            result.append(form)
    return " ".join(result)

if __name__ == "__main__":
    main()