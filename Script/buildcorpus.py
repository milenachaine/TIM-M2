#!/bin/env python3

import glob, xml.etree.ElementTree as ET
from treetagger import TreeTagger
tt = TreeTagger(language='french')

alldocs = ET.Element('corpus')
for xmlfile in sorted(glob.glob('../Corpus/Etudiants/*.xml')):
	print('Processing', xmlfile)
	xmlcorpus = ET.parse(xmlfile)
	for doc in xmlcorpus.getroot():
		# print (doc.text)
		text = doc.text      
		doc.text = ''
		textnode = ET.Element('text')
		textnode.text = text
		doc.append(textnode)
		ttnode = ET.Element('treetagger')
		ttnode.text = ' '.join(['/'.join(ttline) for ttline in tt.tag(text.replace('/', ' '))])
		doc.append(ttnode)
		alldocs.append(doc)

print('Output file')
ET.ElementTree(alldocs).write('../Corpus/all.xml', encoding="UTF-8")
