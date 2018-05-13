#!/bin/env python3

import re

features = {
	'presse': 'numeric',
	'presses': 'numeric',
	'On' : 'numeric',
	'on' : 'numeric',
	'vous': 'numeric',
	'Vous': 'numeric',
	#'suspen': 'numeric',
	'vs': 'numeric',
	'selon': 'numeric',
	'Selon': 'numeric',
	#'superlatif':'numeric',
	'énorme':'numeric',
	'géant':'numeric',
	'grand':'numeric',
	'ameri': 'numeric',
	'American': 'numeric',
	'Americans': 'numeric',
	'nous': 'numeric',
	'Nous': 'numeric',
	#'ponctuation' : 'numeric',
	',':'numeric',
	'?':'numeric',
	'!':'numeric',
	'.':'numeric',
	#'.':'numeric',
	'Corée': 'numeric',
	'coréen':'numeric',
	'bande':'numeric',
	'Chine': 'numeric',
	'adv' : 'numeric',
#	'référendum': 'numeric',
	'onu': 'numeric',
	'ONU':'numeric',
	'russe':'numeric',
	'Russe':'numeric',
	'Russes':'numeric',
	'russes':'numeric',
}

def getfeature(doc, name):
	text = doc.find('text').text
	tt = doc.find('treetagger').text
	#tokenlst = [tok.split('/') for tok in tt.split(' ')]
	text = re.split(r'[;.?]',txt)
	# sandra
	if name == 'presse':
		nbpresse = 0
		nbpresse += text.count('presse')
		nbpresse += text.count('presses')
		return nbpresse
	# abdenour
	# agathe
	if name == 'On':
		nbon = 0
		nbon += text.count(' on ')
		nbon += text.count('On ')
		return nbon
	# andrea
	if name == 'vous':
		nbvous = 0
		nbvous += text.count(' vous ')
		nbvous += text.count('Vous ')
		return nbvous
	if name == 'suspen':
		nbsuspen = 0
		nbsuspen += text.count('...')
		nbsuspen += text.count('…')
		return nbsuspen
	# arthur
	if name == 'vs':
		vs = 0
		vs += text.count('vous')
		vs += text.count('Vous')
		return vs
	if name == 'selon':
		nbselon = 0
		nbselon += text.count('Selon')
		nbselon += text.count('selon')
		return nbselon
	# audrey
	# chloe
	if name == 'superlatif':
		nbsuper = 0
		nbsuper += text.count('énorme')
		nbsuper += text.count('géant')
		nbsuper += text.count('grand')
		return nbsuper
	# damien
	if name == 'ameri':
		nbameri = 0
		for token in tokenlst:
			if token[0].lower().startswith('améri'):
				nbameri += 1
		return nbameri
	if name == 'impers':
		nbimpers = 0
		for token in tokenlst:
			if token[2] in ['on', 'nous']:
				nbimpers += 1
		return nbimpers
	if name == 'ponctuation':
		nbponct = 0
		for token in tokenlst:
			if token[1] == 'PUN':
				nbponct += 1
		return nbponct
	# giovanna
	# guanhua
	if name == 'Corée':
		nbcoree = 0
		nbcoree += text.count('Corée')
		nbcoree += text.count('coréen')
		return nbcoree
	# jielei
	if name == 'bande':
		if 'bande' in text:
			return 1
		return 0
	# mingqiang
	if name == 'Chine':
		if 'Chine' in text:
			return 1
		return 0
	# morgane
	if name == 'adv':
		pattern = re.compile(r'.ment\b')
		nbadv = len(pattern.findall(text))
		return nbadv
	# nico
	if name == 'référendum':
		if 'ONU' in text:
			return 1
		return 0
	# sotiria
	if name == 'onu':
		if 'ONU' in text:
			return 1
		return 0
	if name == 'ponctuation':
		nbponct = 0
		nbponct += text.count('.')
		nbponct += text.count(',')
		nbponct += text.count('!')
		return nbponct
	# xi
	# yousef
	# yunbei
	if name =='russe':
		nbrusse = 0
		path = re.compile(r'(R|r)usse(s)?')
		match = path.findall(text)
		return(len(match))
	# yuran
	return None
