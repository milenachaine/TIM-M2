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
    arff = open("test.arff", 'w')

    # read dataset and generate test arff
    xml_corpus = ET.parse(args.input)
    docs = xml_corpus.getroot().getchildren()
    arff.write("@RELATION fakenews" + '\n')
    functions = [func[1] for func in inspect.getmembers(getfeatures, inspect.isfunction)]
    for func in functions:
        arff.write("@ATTRIBUTE {} numeric".format(str(func.__name__)) + '\n')
    arff.write("@ATTRIBUTE CLASS {fake, trusted, parodic}" + '\n')
    arff.write("@DATA" + '\n')
    for doc in docs:
        feats = [str(func(doc.find("text").text)) for func in functions]
        feats.append(doc.get("class"))
        arff.write(','.join(feats) + '\n')

    arff.close()

    # load test arff into weka
    loader = Loader(classname="weka.core.converters.ArffLoader")
    test = loader.load_file("test.arff")
    test.class_is_last()

    # load classifier
    classifier = Classifier(jobject=serialization.read(args.model))
    classifier.build_classifier(test)

    # output predictions
    for index, inst in enumerate(test):
        pred = classifier.classify_instance(inst)
        docs[index].set('classpredict', inst.class_attribute.value(int(pred)))
    xml_corpus.write(open(args.output, 'w'), encoding="unicode", xml_declaration=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Outputs the predicted class from a test set.")
    parser.add_argument("input", metavar="INPUT", help="the input dataset")
    parser.add_argument("model", metavar="MODEL", help="the model name")
    parser.add_argument("output", metavar="OUTPUT", help="the output dataset")
    args = parser.parse_args()
    try:
        jvm.start()
        main(args)
    except Exception as e:
        print(traceback.format_exc())
    finally:
        jvm.stop()