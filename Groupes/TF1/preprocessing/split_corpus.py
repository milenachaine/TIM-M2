#!/bin/env python3

import os.path, argparse
import xml.etree.ElementTree as ET

aparser = argparse.ArgumentParser(description='Split corpus')
aparser.add_argument('-m', '--mode', default='test', help='Choices : test')
aparser.add_argument('input', help='Input file')
args = aparser.parse_args()

print('Reading input corpus')
xmlcorpus = ET.parse(args.input)
inputbn, inputext = os.path.splitext(args.input)

if args.mode == 'test':

	print('Split docs')
	traincorpus = ET.Element('corpus')
	testcorpus = ET.Element('corpus')
	docs = xmlcorpus.getroot().getchildren()
	for i in range(len(docs)):
		corpuspart = traincorpus
		if docs[i].get('split') == 'test':
			corpuspart = testcorpus
		corpuspart.append(docs[i])

	print('Writing to files')
	ET.ElementTree(traincorpus).write(open(inputbn+'-train'+inputext, 'w'), encoding='unicode')
	ET.ElementTree(testcorpus).write(open(inputbn+'-test'+inputext, 'w'), encoding='unicode')
