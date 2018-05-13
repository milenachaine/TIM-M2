#!/bin/env python3
'''
	Auteurs : FAVIA Giovanna - HELMAN Agathe - SCARCELLA Nicolas
	Date : AVRIL 2018
	
	Ce programme répertorie les features qui seront appliquées sur les corpus italiens d'entrainement et de test lors de l'appel des programmes train.py et predict.py.
	
	Lancement: python3 racinisation.py fr_corpus.xml
	
'''
import re
features = {
	'virgolette':'numeric',
	'titre':'numeric',
	'politique':'numeric',
	'foreign':'numeric',
	'italiano':'numeric',
	'facebook':'numeric',
	'adverbe':'numeric',
	'punctuation':'numeric',
	'pays':'numeric',
	'milioni':'numeric',
	'governo':'numeric',
	'NPR':'numeric',
	'presidente':'numeric',
}
def getfeature(doc, name):
	text = doc.find('text').text
	titre=doc.attrib.get('title')

	#recherche dans les du titre
	treetagger_title = doc.find('treetagger_title').text
	
	#recherche dans les balises bigrams
	bigrams = doc.find('bigrams').text
	treetagger = doc.find('treetagger').text
	lemme_POS_titre=treetagger_title.split('/ ')

	#recherche dans les balises treetagger
	lemme_POS=treetagger.split('/ ')
######################################################################
	#punctuation sur les titres
	if name == "virgolette":
		nbvirgolette = 0
		nbvirgolette += titre.count('\'')
		return nbvirgolette

	if name == 'titre':
		nbtitre=0
		for i in range(0, len(lemme_POS_titre)-1):
			lemme_titre, pos_titre = lemme_POS_titre[i].split()
			if pos_titre=='ADJ':
				nbtitre+=1
		return nbtitre

	if name == "politique":
		nbpolitique = 0
		nbpolitique += bigrams.count('(di maio)')
		nbpolitique += bigrams.count('(stato uniti)')
		return nbpolitique
	
	if name == "foreign":
		nbpolitique = 0
		nbpolitique += bigrams.count('(foreign fighters)')
		return nbpolitique

	# pour FAKE
	if name == 'italiano':
		nbitaliano = 0
		for token in lemme_POS:
			lemme, pos = token.split()
			if lemme == 'italiano':
				nbitaliano += 1
		return nbitaliano

	if name == 'facebook':
		nbfacebook = 0
		for token in text:
			if token == 'Facebook':
				nbfacebook += 1
		return nbfacebook

	if name == 'adverbe':
		nbadv = 0
		for token in lemme_POS:
			lemme, pos = token.split()
			if pos == 'ADV':
				nbadv += 1
		return nbadv

	# TRUSTED et PARODIC
	if name == 'punctuation':
		nbsuspen = 0
		nbsuspen += text.count('?')
		nbsuspen += text.count('!')
		nbsuspen += text.count('"')
		return nbsuspen

	# FAKE
	if name == 'pays':
		nbpays=0
		for i in range(0, len(lemme_POS)-1):
			lemme1, pos1 = lemme_POS[i].split()
			lemme2, pos2 = lemme_POS[i+1].split()
			if pos1=='NPR' and pos2=='PON':
				nbpays+=1
		return nbpays

	if name == 'milioni':
		nbmilioni=0
		for i in range(0, len(lemme_POS)-1):
			lemme1, pos1 = lemme_POS[i].split()
			lemme2, pos2 = lemme_POS[i+1].split()
			if pos1=='NUM' and lemme2=='milioni':
				nbmilioni+=1
		return nbmilioni

	if name == 'governo':
		nbgoverno=0
		for token in lemme_POS:
			lemme, pos = token.split()
			if lemme == 'governo':
				nbgoverno += 1
		return nbgoverno
	#NOMS PROPRES
	if name == 'NPR':
		nbNPR=0
		for i in range(0, len(lemme_POS)-1):
			lemme, pos = lemme_POS[i].split()
			if pos=='NPR':
				nbNPR+=1
		return nbNPR

	if name == 'presidente':
		nbpresidente=0
		for i in range(0, len(lemme_POS)-1):
			lemme1, pos1 = lemme_POS[i].split()
			lemme2, pos2 = lemme_POS[i+1].split()
			if lemme1=='presidente' and pos2=='ADJ':
				nbpresidente+=1
		return nbpresidente
	return None