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

""" transformation du format liste de dictionnaires en data frame pandas afin de calculer le tf-idf """

# le chemin vers tous les fichiers conll

folder_path = glob.glob("/Users/ferialyahiaoui/Documents/cours/TIM-M2/Groupes/Pretraitement/Corpus/net-iris/*/*/*/*.conll")

#folder_path = glob.glob("/Users/ferialyahiaoui/Documents/cours/*.conll")



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
		#print(filename.group())
		with open(p, 'r') as files:
		# à chaque passage d'un fichier lu
			listlem = []
			dico_q = {}

		
			for file in files:
				cols = file.rstrip('\n').split('\t')
				if len(cols) == 3:
				# on ajoute la colonnes des lemmes dans une liste
					listlem.append(cols[2])
			#print(istlem)
		# on parcourt la liste des id des fichiers 
				for filename in id_fi:
			# on crée une liste de dictionnaires avec comme clé : id dont la valeur est id_fic et une autre clé questions et comme valeur : liste de lemmes du fic en question
					#dico_q[filename] = istlem
					dico_q['id'] = filename
					dico_q['questions'] = listlem
				
				




	# puis, on met toutes les listes des lemmes dans une liste globale
		#lists.append(listlem)
		liste_q.append(dico_q)

#print(lists)
#print('\n')
#print(liste_q)
test_dataframe = pd.DataFrame(liste_q)
#print(id_fi)
print("Format de la dataframe :\n{}".format(test_dataframe))

				

