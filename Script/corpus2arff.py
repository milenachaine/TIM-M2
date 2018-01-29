#!/bin/env python3

import xml.etree.ElementTree as ET

features = {
	# sandra
	# abdenour
	# agathe
	# andrea
	# arthur
	# audrey
	# chloe
	# damien
	'ameri': 'numeric',
	'impers': 'numeric',
	# giovanna
	# guanhua
	'Corée': 'numeric',
	# jielei
	# mingqiang
	# morgane
	# nico
	# xi
	# yousef
	# yunbei
	# yuran
}

def getfeature(text, name):
	# sandra
	# abdenour
	# agathe
	# andrea
	# arthur
	# audrey
	# chloe
	# damien
	if name == 'ameri':
		if 'Améri' in text:
			return 1
		return 0
	if name == 'impers':
		nbimpers = 0
		nbimpers += text.count('on')
		nbimpers += text.count('nous')
		return nbimpers
	# giovanna
	# guanhua
	if name == 'Corée':
		nbcoree = 0
		nbcoree += text.count('Corée')
		nbcoree += text.count('coréen')
		return nbcoree
	# jielei
	# mingqiang
	# morgane
	# nico
	# xi
	# yousef
	# yunbei
	# yuran
	return None

print('Initialize arff files')
header = ''
header += '@relation fakevstrusted\n'
for f in features:
	header += '@attribute '+f+' '+features[f]+'\n'
header += '@attribute class {fake,trusted}\n'
header += '@data\n'

arfffiletrain = open('../Corpus/train.arff', 'w')
arfffiletrain.write(header)
arfffiletest = open('../Corpus/test.arff', 'w')
arfffiletest.write(header)

print('Reading corpus and finding attributes')
xmlcorpus = ET.parse('../Corpus/all.xml')
nodoc = 0
for doc in xmlcorpus.getroot():
	text = doc.text.strip()
	attrs = ','.join(str(getfeature(text, f)) for f in features)+','+doc.get('class')
	if nodoc%3:
		arfffiletrain.write(attrs+'\n')
	else:
		arfffiletest.write(attrs+'\n')
	nodoc += 1
