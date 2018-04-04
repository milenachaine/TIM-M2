#!/bin/env python3

import argparse, traceback
import xml.etree.ElementTree as ET
import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier
import weka.core.serialization as serialization
from getfeatures import features, getfeature

def main(args):
    arff = open("test.arff", 'w')

    # read dataset and generate test arff
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
    xmlcorpus.write(open(args.output, 'w'), encoding="unicode", xml_declaration=True)

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