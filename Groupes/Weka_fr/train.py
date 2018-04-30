#!/bin/env python3
# -*- coding: utf8 -*-

import argparse, traceback, inspect
import xml.etree.ElementTree as ET
import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier
import weka.core.serialization as serialization
import getfeatures

def main(args):
    arff = open("train.arff", 'w')

    # read dataset and generate train arff
    xml_corpus = ET.parse(args.input)
    docs = xml_corpus.getroot().getchildren()
    arff.write("@RELATION fakenews" + '\n')
    functions = [func[1] for func in inspect.getmembers(getfeatures, inspect.isfunction)]
    for func in functions:
        arff.write("@ATTRIBUTE {} NUMERIC".format(str(func.__name__)) + '\n')
    arff.write("@ATTRIBUTE CLASS {fake, trusted, parodic}" + '\n')
    arff.write("@DATA" + '\n')
    for doc in docs:
        text = doc.find("text").text
        lemmas = [tok.split('/')[2] for tok in doc.find("treetagger").text.split(' ')]
        feats = [str(func(text, lemmas)) for func in functions]
        feats.append(doc.get("class"))
        arff.write(','.join(feats) + '\n')

    arff.close()

    # load train arff into weka
    loader = Loader(classname="weka.core.converters.ArffLoader")
    train = loader.load_file("train.arff")
    train.class_is_last()

    # build classifier
    classifier = Classifier(classname="weka.classifiers.bayes.NaiveBayesMultinomial")
    classifier.build_classifier(train)

    # save classifier
    serialization.write(args.model, classifier)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trains a classifier on a training set.")
    parser.add_argument("input", metavar="INPUT", help="the input dataset")
    parser.add_argument("model", metavar="MODEL", help="the model name")
    args = parser.parse_args()
    try:
        jvm.start()
        main(args)
    except Exception as e:
        print(traceback.format_exc())
    finally:
        jvm.stop()
