#!/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse('../Corpus/all.xml')
corpus = tree.getroot()
for doc in corpus:
    print(doc)
    if 'class' in doc.attrib:
        print(doctext.text)
        print(doc.attrib['class])
