#!/bin/env python3

import argparse
import xml.etree.ElementTree as ET

aparser = argparse.ArgumentParser(description='Evaluate corpus')
aparser.add_argument('input', help='Input file')
args = aparser.parse_args()

print('Reading input corpus')
xmlcorpus = ET.parse(args.input)
docs = xmlcorpus.getroot().getchildren()
nbdocs = len(docs)
success = 0
for i in range(nbdocs):
	if docs[i].get('class') == docs[i].get('classpredict'):
		success += 1

print('Accuracy: ', success/nbdocs)
