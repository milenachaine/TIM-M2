# -*- coding: UTF-8 -*-

#import xml.etree.ElementTree as ET
#import os
#import sys
#import nltk
# from nltk.tokenize import RegexpTokenizer
# tokenizer = RegexpTokenizer(r'\w+')

# from nltk.corpus import stopwords
# stopWords = set(stopwords.words('french'))

# Exemple en bas
# from nltk.stem import SnowballStemmer
# stemmer = SnowballStemmer("french")

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics, feature_extraction

import pickle


# path = '../../Similarite/'
path = '/home/teamlaw/git-TIM-M2/Groupes/Similarite/'
documents_Corpus = pickle.load(open(path+"documents_Corpus.pkl", "rb"))
vectorizer = pickle.load(open(path+"vectorizer.pkl", "rb"))
TfIdfQuestions = pickle.load(open(path+"TfIdfQuestions.pkl", "rb"))
liste_questions = pickle.load(open(path+"liste_questions.pkl", "rb"))

DOC_CLASS = {
	"imm": "immobilier",
	"trv": "travail",
	"per": "personne et famille",
	"fin": "finances, fiscalité et assurance",
	"soc": "rapports à la société",
	"jus": "monde de la justice",
	"ent": "entreprise",
	"int": "internet, téléphonie et prop. intellectuelle"
}

from make_prediction import *
def predict(model, phrase):
	"""
		Make prediction : catégorisation (code de Chunyang et Yzhou)
	"""
	path_to_model = path+model
	phrase_to_predict = phrase

	# load the model in memory with the function load_model
	# you only need to load the model once (if you don't intend to change
	# another model)
	model = load_model(path_to_model)

	# make prediction for a phrase with the funciton make_prediction
	# can loop this for more predictions
	predicted_class = make_prediction(model, phrase_to_predict)

	return predicted_class


def getBestQuestion(question_utilisateur):
	"""Catégorisation"""
	#On appelle le script de Chunyang et Yizhou
	classe_question = predict("model_class_question_uti", question_utilisateur)
	#On développe l'abbreviation remontée
	classe_question = DOC_CLASS[classe_question]

	"""Similarité"""
	TfIdfQuestions_utilisateur = vectorizer.transform([question_utilisateur], True)

	bestQuestionScore = None
	bestQuestionIndex = None
	#On parcours la liste des questions
	for questionIndex in range(len(liste_questions)):
		# On ne garde que les question dont la classe coincide avec la prédiction
		index_doc = "iris" + str(questionIndex + 1)
		if documents_Corpus.get(index_doc)['class'].lower() == classe_question:
			#On calcul la similarité de la question avec le query de l'utilisateur
			simScore = metrics.pairwise.cosine_similarity(TfIdfQuestions[questionIndex], TfIdfQuestions_utilisateur[0])
			#On note la question la plus similaire
			if not bestQuestionScore or simScore > bestQuestionScore:
				bestQuestionScore = simScore
				bestQuestionIndex = questionIndex


	if (bestQuestionIndex):
		index = "iris" + str(bestQuestionIndex)
		return documents_Corpus.get(index)
