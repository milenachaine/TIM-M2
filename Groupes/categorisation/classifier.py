"""Classifier of legal textual documents.



"""
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

from settings import *

import pickle


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
    vectorizer = TfidfVectorizer(
        max_features=int(args.feature_size) if args.feature_size else FEATURE_SIZE
    )
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
        choices=["token","lemma","lemma+pos","ngram"],
        default="token",
        help=FEAT_HELP
    )
    parser.add_argument('-s', "--feature_size")
    parser.add_argument('-o', "--output")
    return parser.parse_args()

def prepare_data(FI,feat):
    corpus = pickle.load(file=open(FI,"rb"))
    X = list()
    Y = list()
    for doc in corpus:
        Y.append(doc.class_)
        X.append(FEAT[feat](doc))
    return (X,Y)

def get_token(doc):
    return " ".join(doc.question.text)

def get_lemma(doc):
    return " ".join(doc.question.lemma)

def get_lp(doc):
    return " ".join([t[1]+"/"+t[2] for t in doc.question.tagged_text()])

def get_ngram(doc):
    pass

FEAT = {
    "token": get_token,
    "lemma": get_lemma,
    "lemma+pos": get_lp,
    "ngram": get_ngram,
}

if __name__ == "__main__":
    main()