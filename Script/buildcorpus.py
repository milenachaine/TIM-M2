#!/bin/env python3

import xml.etree.ElementTree as ET
# from treetagger import TreeTagger
# tt = TreeTagger(language='french')

docids = {}
alldocs = ET.Element('corpus')
for etudiant in open('../Corpus/etudiants.lst').readlines():
	etudiantid = etudiant.strip()
	xmlfile = '../Corpus/Etudiants/Categorisation/'+etudiantid+'.xml'
	print('Processing', xmlfile)
	xmlcorpus = ET.parse(xmlfile)
	etudiantdoc = 0
	for doc in xmlcorpus.getroot():
		etudiantdoc += 1
		docid = etudiantid+str(etudiantdoc)
		doc.attrib['id'] = docid
		text = doc.text
		textnode = ET.Element('text')
		textnode.text = text
		doc.append(textnode)
		doc.text = ''
		# ttnode = ET.Element('treetagger')
		# text = text.replace('/', ' ')
		# text = text.replace('’', '\'')
		# ttnode.text = ' '.join(['/'.join(ttline) for ttline in tt.tag(text)])
		# doc.append(ttnode)
		alldocs.append(doc)

print('Output file')
ET.ElementTree(alldocs).write('../Corpus/categorisation.xml', encoding="UTF-8")
