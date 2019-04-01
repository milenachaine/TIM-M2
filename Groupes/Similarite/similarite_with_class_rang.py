import xml.etree.ElementTree as ET

import nltk

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

from nltk.corpus import stopwords
stopWords = set(stopwords.words('french'))

# Exemple en bas
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("french")

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics, feature_extraction

import os
import sys


DOC_CLASS = {
    "immobilier": "imm",
    "travail": "trv",
    "personne et famille": "per",
    "finances, fiscalité et assurance": "fin",
    "rapports à la société": "soc",
    "monde de la justice": "jus",
    "entreprise": "ent",
    "internet, téléphonie et prop. intellectuelle": "int"
}

"""

    Make prediction : catégorisation (code de Chunyang et Yzhou)

"""


from make_prediction import *

def predict(model, phrase):

    path_to_model = model
    phrase_to_predict = phrase

    # load the model in memory with the function load_model
    # you only need to load the model once (if you don't intend to change
    # another model)
    model = load_model(path_to_model)

    # make prediction for a phrase with the funciton make_prediction
    # can loop this for more predictions
    predicted_class = make_prediction(model, phrase_to_predict)

    return predicted_class



"""

    Intéraction utilisateur :

        - On récupère la question à travers l'input


"""

question_utilisateur = input("Posez une question : ")

assert(question_utilisateur != "")
print("Votre question est : ", question_utilisateur)


classe_question = predict("model_class_question_uti", question_utilisateur)


for cat, abb in DOC_CLASS.items():
    if abb == classe_question:
        classe_question = cat

print("Classe prédite pour la question utilisateur : ", classe_question)

"""

    Similarité

"""


import pickle

documents_Corpus = pickle.load(open("documents_Corpus.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
TfIdfQuestions = pickle.load(open("TfIdfQuestions.pkl", "rb"))
liste_questions = pickle.load(open("liste_questions.pkl", "rb"))


TfIdfQuestions_utilisateur = vectorizer.transform([question_utilisateur], True)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics, feature_extraction

bestQuestionScore = None
bestQuestionIndex = None
listeQuestionScore = {}
for questionIndex in range (len(liste_questions)):
    #print("    Question: ",liste_questions[questionIndex])
    # Ici on vérifie que la classe du document est bien celle qu'on veut
    index_doc = "iris" + str(questionIndex + 1)
    if documents_Corpus.get(index_doc)['class'].lower() == classe_question:

        simScore = metrics.pairwise.cosine_similarity(TfIdfQuestions[questionIndex], TfIdfQuestions_utilisateur[0])
        #print ("        simScore: ",simScore)
        listeQuestionScore[index_doc] = simScore
        if not bestQuestionScore or simScore > bestQuestionScore:
            bestQuestionScore = simScore
            bestQuestionIndex = questionIndex

print("  ===> Best Question : ")
if (bestQuestionIndex):
    index = "iris" + str(bestQuestionIndex)
    #print("       QuestionIndex : ",bestQuestionIndex," => ", documents_Corpus.get(index))

sim = sorted(listeQuestionScore.values(), reverse = True)[:10]



for i in range(0, len(sim)):
    score_sim = sim[i]
    for key, value in listeQuestionScore.items():
        if score_sim == value:
            index = key

    print("Question Index : ", index, "= > ", documents_Corpus.get(index)['answers'])
    print("\n       --------------        \n")
