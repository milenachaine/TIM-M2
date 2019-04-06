#!/usr/bin/python3
# -*- coding: utf-8 -*

""" programme qui parcours tous les fichiers conll
il garde en mémoire la liste des fichiers. Ces derniers sont les clés d'un dictionnaire dont les valeurs sont la liste des lemmes de chaque fichier.
Aussi, on met dans une liste globale les listes des lemmes de chaque fichier conll. """

import os
import glob
import re

# le chemin vers tous les fichiers conll

folder_path = glob.glob("/Users/ferialyahiaoui/Documents/cours/TIM-M2/Groupes/Pretraitement/Corpus/net-iris/*/*/*/*.conll")

#folder_path = glob.glob("/Users/ferialyahiaoui/Documents/cours/*.conll")



id_fi = []
lists = []
dico_q = {} # dico des questions : clé : id_fichier, valeur : liste des lemmes


#pat1 = re.compile('iris([0-9]{3,5})_q([0-9]{1,3})\.conll$')

pat = re.compile("iris[0-9]{3,5}_[q|a].+\.conll$")



# on parcourt la liste des chemins des fichiers conll
for p in folder_path:

	# l'identifiant d'un fichier correpond à cette regex
	filename = pat.search(p)
	if filename:
		id_fi.append(filename.group())
		#print(filename.group())
#print(id_fi)

	# on récupère chaque id et on le met dans une liste 
	
	# pour chaque fichier lu
	
	with open(p, 'r') as files:
		# à chaque passage d'un fichier lu
		lists_w = []

		
		for file in files:
			cols = file.rstrip('\n').split('\t')
			if len(cols) == 3:
				# on ajoute la colonnes des lemmes dans une liste
				lists_w.append(cols[2])
		#print(lists_w)
		# on parcourt la liste des id des fichiers 
		for filename in id_fi:
			# on crée un dic avec comme clé : id_fic et comme valeur : liste de lemmes du fic en question
			dico_q[filename] = lists_w

	# puis, on met toutes les listes des lemmes dans une liste globale
	lists.append(lists_w)
print(lists)
print('\n')
print(dico_q)
