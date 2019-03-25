### Ce package dépend de la liste des mots "list_terms.txt"

dicoTerms = {}

def constructDico(listPath):
"""Charger le dictionnaire dans la mémoire"""
	global dicoTerms
	with open(listPath, 'r') as f:
		for line in f:
			line = line.strip()
			items = line.split('\t')
			if len(items) == 2:
				if items[0] not in dicoTerms.keys():
					dicoTerms[items[0]] = items[1]
				
def bold(s):
"""Transformer une chaîne de caractères brute en une chaîne qui contient des balises au tour des mots-clés s'il en existe. """
	global dicoTerms
	tokens = s.split()
	result = ""
	for token in tokens:
		### Les clés du dicoTerms sont déjà été mises en minuscules lors de la création de la liste des termes. 
		if token.lower() in dicoTerms.keys():
			token = "<b><a href=\"" + dicoTerms[token.lower()] + "\">" + token + "</a></b>"
		result = result + ' ' + token
		
	return result

			