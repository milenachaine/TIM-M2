#!/bin/env python3
'''
	Auteurs : FAVIA Giovanna - HELMAN Agathe - SCARCELLA Nicolas
	Date : AVRIL 2018
	
	Ce programme répertorie les features qui seront appliquées sur les corpus français d'entrainement et de test lors de l'appel des programmes train.py et predict.py.
	
	Lancement: python3 racinisation.py fr_corpus.xml
	
'''
import re
# Liste des features dans l'ordre des conditions et "xxxx":"numeric" == if name == "xxx"
features = {
# NOM => TRUE or FALSE
	'ponctuation':'numeric',
	'negation':'numeric',
	'etranger':'numeric',
	'NWO':'numeric',
	'national':'numeric',
	'terrorisme':'numeric',
	'Trump':'numeric',
	'antisemite':'numeric',
	'banque':'numeric',
	'finance':'numeric',
}
def getfeature(doc, name):
	text = doc.find('texte').text
	rad = doc.find('racinisation').text
	# Features pour ponctuation
	if name == 'ponctuation':
		nb_ponct = 0
		nb_ponct += rad.count("!")
		nb_ponct += rad.count("?")
		nb_ponct += rad.count("«")
		nb_ponct += rad.count("»")
		return nb_ponct
	# Features pour négation
	if name == 'negation':
		nb_neg = 0
		nb_neg += rad.count("ne")	
		nb_neg += rad.count("pas")	
		return nb_neg
	# Features pour substantifs (racines)
	if name == 'etranger':
		return rad.count("étranger")
	if name == 'NWO': 
		return rad.count("nouvel ordre mondial")
	if name == 'national':
		return rad.count("national")
	if name == 'terrorisme':
		return rad.count("terror")
	if name == 'Trump':
		nb_trump = 0
		nb_trump += rad.count("Trump")	
		nb_trump += rad.count("trump")
		return nb_trump
		# motif = re.compile("^(T|t)rump") # Trump est mentionné avec et sans majuscule
		# reperage = motif.findall(rad)
		# nb_trump += reperage
		# return (len(reperage))
	if name == 'antisemite':
		nb_antisemite = 0
		nb_antisemite += rad.count("antisémit")
		# return rad.count("antisemit")
		return nb_antisemite
	if name == 'banque':
		motif = re.compile("banqu") # Malheureusement, le radical de Snowball est universitair ce qui exclut le mot université.
		reperage = motif.findall(rad)
		return (len(reperage))
	if name == 'finance':
		motif = re.compile("financi?") # Il y a deux racines: financ et financi.
		reperage = motif.findall(rad)
		return (len(reperage))
	return None