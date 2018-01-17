#!/bin/env python3

import glob

import xml.etree.ElementTree as ET

for xmlfile in glob.glob('../Corpus/*.xml'):
	print('Opening', xmlfile)
	xmlcorpus = ET.parse(xmlfile)
	print(xmlcorpus)

