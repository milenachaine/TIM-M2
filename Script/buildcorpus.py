#!/bin/env python3

import xml.etree.ElementTree as ET
from treetagger import TreeTagger
tt = TreeTagger(language='french')

alldocs = ET.Element('corpus')
for etudiant in open('../Corpus/etudiants.lst').readlines():
	xmlfile = '../Corpus/Etudiants/'+etudiant.strip()+'.xml'
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
		text = text.replace('/', ' ')
		text = text.replace('’', '\'')
		ttnode.text = ' '.join(['/'.join(ttline) for ttline in tt.tag(text)])
		doc.append(ttnode)
		alldocs.append(doc)

print('Output file')
ET.ElementTree(alldocs).write('../Corpus/all.xml', encoding="UTF-8")
