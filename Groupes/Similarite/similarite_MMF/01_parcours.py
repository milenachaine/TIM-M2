#!/usr/bin/python3
# -*- coding: utf-8 -*

# premier test parcours
# input pour récupérer le chemin + des print pour vérifier que ça marche
import os
import sys
import glob
import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
import pickle



sep = "-"*70
message = "Usage : python3 {} <dossier comportant le corpus>".format(sys.argv[0])
if len(sys.argv) != 2:
	print(sep)
	print("Nombre d'arguments incorrect")
	print(message)
	print(sep)
	exit()
elif not glob.glob(sys.argv[1]):
	print(sep)
	print("{} est introuvable".format(sys.argv[1]))
	print(message)
	print(sep)
	exit()
else:
	print(sep)
	print("Création d'une dataframe contenant le corpus dans corpuspd.pkl")
	print(sep)

path = sys.argv[1] + "/*/*/*/*.conll"
print("Chemin vers le corpus : {}".format(path))
folder_path = glob.glob(path)

#folder_path = glob.glob("/Users/ferialyahiaoui/Documents/cours/corpus-test/*/*.conll")



id_fi = []

liste_q = [] # liste globale des dico des questions



pat = re.compile("iris[0-9]{3,5}_q.+\.conll$")



# on parcourt la liste des chemins des fichiers conll
for p in folder_path:

	# l'identifiant d'un fichier correpond à cette regex
	filename = pat.search(p)
	if filename:
		id_fi.append(filename.group())
		with open(p, 'r') as files:
			print("Fichier ouvert : {}".format(p))
		# à chaque passage d'un fichier lu
			listlem = []
			listw = []
			listpos = []
			dico_q = {}

		
			for file in files:
				cols = file.rstrip('\n').split('\t')
				if len(cols) == 3: # ici on ignore les liste vides provoquant des erreurs du type : index out of range.
				# on ajoute la colonnes des lemmes dans une liste
					listlem.append(cols[2])
					listw.append(cols[0])
					listpos.append(cols[1])

		# on parcourt la liste des id des fichiers 
				for filename in id_fi:
			# on crée un dic avec plusieurs clés et leurs valeurs 

					
					dico_q['id'] = filename
					dico_q['lemmes'] = listlem
					dico_q['mots'] = listw
					dico_q['pos'] = listpos
				
				




	# puis, on met tous les dic dans une liste globale
		
		liste_q.append(dico_q)

test_dataframe = pd.DataFrame(liste_q)
test_dataframe.to_pickle("./corpuspd.pkl")

print(sep)
print("Format de la dataframe :\n{}".format(test_dataframe.head()))

				

