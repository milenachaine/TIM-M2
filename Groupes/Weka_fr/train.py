#!/bin/env python3

import argparse, traceback
import xml.etree.ElementTree as ET
import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier
import weka.core.serialization as serialization
from getfeatures import features, getfeature

def main(args):
    arff = open("train.arff", 'w')

    # read dataset and generate train arff
    xmlcorpus = ET.parse(args.input)
    docs = xmlcorpus.getroot().getchildren()
    featurekeys = sorted(list(features.keys()))
    arff.write("@relation fakevstrusted" + '\n')
    for feature in featurekeys:
        arff.write("@attribute " + feature + " numeric" + '\n')
    arff.write("@attribute class {fake,trusted,parodic}" + '\n')
    arff.write("@data\n")
    for i in range(len(docs)):
        docfeatures = []
        for j in range(len(featurekeys)):
            doc = docs[i]
            featurename = featurekeys[j]
            docfeatures.append(str(getfeature(doc, featurename)))
        docfeatures.append(doc.get("class"))
        arff.write(','.join(docfeatures) + '\n')

    arff.close()

    # load train arff into weka
    loader = Loader(classname="weka.core.converters.ArffLoader")
    train = loader.load_file("train.arff")
    train.class_is_last()

    # build classifier
    classifier = Classifier(classname="weka.classifiers.trees.J48")
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