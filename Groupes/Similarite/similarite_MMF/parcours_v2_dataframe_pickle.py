#!/usr/bin/python3
# -*- coding: utf-8 -*

# premier test parcours
import os
import glob
import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
import pickle

# le chemin vers tous les fichiers conll

#folder_path = glob.glob("/Users/ferialyahiaoui/Documents/cours/TIM-M2/Groupes/Pretraitement/Corpus/net-iris-copie/*/*/*/*.conll")

folder_path = glob.glob("/Users/ferialyahiaoui/Documents/cours/corpus-test/*/*.conll")



id_fi = []
lists = []
liste_q = [] # dico des questions : clé : id_fichier, valeur : liste des lemmes

dic_q_r = {}

str_m1 = []
str_m2 = []



pat = re.compile("iris[0-9]{3,5}_q.+\.conll$")



# on parcourt la liste des chemins des fichiers conll
for p in folder_path:

	# l'identifiant d'un fichier correpond à cette regex
	filename = pat.search(p)
	if filename:
		id_fi.append(filename.group())
		with open(p, 'r') as files:
		# à chaque passage d'un fichier lu
			listlem = []
			listw = []
			dico_q = {}

		
			for file in files:
				cols = file.rstrip('\n').split('\t')
				if len(cols) == 3:
				# on ajoute la colonnes des lemmes dans une liste
					listlem.append(cols[2])
					listw.append(cols[0])
			#print(istlem)
		# on parcourt la liste des id des fichiers 
				for filename in id_fi:
			# on crée un dic avec comme clé : id_fic et comme valeur : liste de lemmes du fic en question
					#dico_q[filename] = istlem
					dico_q['id'] = filename
					dico_q['lemmes'] = listlem
					dico_q['mots'] = listw
				
				




	# puis, on met toutes les listes des lemmes dans une liste globale
		#lists.append(listlem)
		liste_q.append(dico_q)

#print(lists)
#print('\n')
#print(liste_q)
test_dataframe = pd.DataFrame(liste_q)
test_dataframe.to_pickle("./corpuspd.pkl")
#print(id_fi)
print("Format de la dataframe :\n{}".format(test_dataframe))

				

