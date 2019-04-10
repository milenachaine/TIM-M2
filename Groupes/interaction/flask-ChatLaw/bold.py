# -*- coding: UTF-8 -*-
### Ce package dépend de la liste des mots "list_terms.txt"

def constructDico(listPath):
	"""Charger le dictionnaire dans la mémoire"""
	dicoTerms = {}
	with open(listPath, 'r', encoding='utf8') as f:
		for line in f:
			line = line.strip()
			items = line.split('\t')
			if len(items) == 2:
				if items[0] not in dicoTerms.keys():
					dicoTerms[items[0]] = items[1]
	return dicoTerms

def cut(s, dico):
	dicoTerms = dico
	result = [] #une liste des tokens, y compris des expressions polylexicales dans le domaine juridique
	index = 0
	tokens = s.split()
	max_index = len(tokens)
	while index < max_index:
		word = None
		for size in range(5, 0, -1):
			if index + size > max_index:
				continue
			pieces = tokens[index:(index + size)] #Un candidat polylexical d'une certaine taille
			piece = ""
			for x in pieces:
				piece = piece + ' ' + x #On met les tokens dans une seule chaîne de caractères "piece" pour faciliter la comparaisons avec le dico qu'on vient de créer
			piece = piece.strip(' ')
			if piece.lower() in dicoTerms.keys():
				word = piece
				result.append(word)
				index = index + size
				break
		if word == None:
			result.append(tokens[index])
			index = index + 1
	return result
		
					
def bold(tokens, dico):
	dicoTerms = dico
	result = ""
	max = len(tokens)
	for i in range(max):
		token = tokens[i]
		### Les clés du dicoTerms sont déjà été mises en minuscules lors de la création de la liste des termes. 
		if token.lower() in dicoTerms.keys():
			if token.lower() == "fait" and i > 0:
				if tokens[i - 1].lower() in ["un", "ce", "le"]:
					token = "<b><a href=\"" + dicoTerms[token.lower()] + "\">" + token + "</a></b>"
			else:
				token = "<b><a href=\"" + dicoTerms[token.lower()] + "\">" + token + "</a></b>"
		result = result + ' ' + token
		
	return result
	
if __name__ == "__main__":
	dicoTerms = {}
	constructDico("./list_terms_2.txt")
	while True:
		x = input()
		out = bold(cut(x))
		print(out)
			