import xml.etree.ElementTree as ET
import pickle
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


#### PREDICTION CLASSE ####

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


question_utilisateur = input("Posez une question : ")

assert(question_utilisateur != "")
print("Votre question est : ", question_utilisateur)

classe_question = predict("model_class_question_uti", question_utilisateur)

for cat, abb in DOC_CLASS.items():
    if abb == classe_question:
        classe_question = cat

print("Classe prédite pour la question utilisateur : ", classe_question)

#### SIMILARITE ####



documents_Corpus = pickle.load(open("documents_Corpus.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
TfIdfQuestions = pickle.load(open("TfIdfQuestions.pkl", "rb"))
liste_questions = pickle.load(open("liste_questions.pkl", "rb"))

question_uti_normalize = ""
for mot in tokenizer.tokenize(question_utilisateur):
    if mot.lower() not in stopWords:
        mot_stem = stemmer.stem(mot.lower()) + " "
        question_uti_normalize += mot_stem

TfIdfQuestions_utilisateur = vectorizer.transform([question_uti_normalize], True)

bestQuestionScore = None
bestQuestionIndex = None
listeQuestionScore = {}

for questionIndex in range (len(liste_questions)):

    # Ici on vérifie que la classe du document est bien celle qu'on veut
    index_doc = "iris" + str(questionIndex + 1)
    if documents_Corpus.get(index_doc)['class'].lower() == classe_question:

        simScore = metrics.pairwise.cosine_similarity(TfIdfQuestions[questionIndex], TfIdfQuestions_utilisateur[0])

        listeQuestionScore[index_doc] = simScore
        if not bestQuestionScore or simScore > bestQuestionScore:
            bestQuestionScore = simScore
            bestQuestionIndex = questionIndex


bestDocs = [index for index in sorted(listeQuestionScore, key=listeQuestionScore.get, reverse=True)][:5]

answers = []
for ind in bestDocs:
    answers.append(documents_Corpus.get(ind)['answers'])

def normalize(text):
    total_normalize = []
    for answer in text:
        pre_answer = []
        for mot in tokenizer.tokenize(answer):
            mot_stem = stemmer.stem(mot.lower())
            pre_answer.append(mot_stem)
        answer_normalize = " ".join(pre_answer)
        total_normalize.append(answer_normalize)

    return total_normalize



answers_normalized = normalize(answers)

pickle.dump(answers, open("answers.pkl", "wb"))
pickle.dump(answers_normalized, open("answers_normalized.pkl", "wb"))

pickle.dump(question_uti_normalize, open("question_uti_normalized.pkl", "wb"))
