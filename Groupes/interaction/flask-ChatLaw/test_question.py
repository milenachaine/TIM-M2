# -*- coding: UTF-8 -*-
import pickle

path = teampath+'/Groupes/Similarite/'
# path = '../../Similarite/'
documents_Corpus = pickle.load(open(path+"documents_Corpus.pkl", "rb"))
vectorizer = pickle.load(open(path+"vectorizer.pkl", "rb"))
TfIdfQuestions = pickle.load(open(path+"TfIdfQuestions.pkl", "rb"))
liste_questions = pickle.load(open(path+"liste_questions.pkl", "rb"))

import nltk
#from nltk.tokenize import RegexpTokenizer
#tokenizer = RegexpTokenizer(r'\w+')
#from nltk.corpus import stopwords
#stopWords = set(stopwords.words('french'))
#from nltk.stem import SnowballStemmer
#stemmer = SnowballStemmer("french")

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics, feature_extraction

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
    model = load_model(model)
    predicted_class = make_prediction(model, phrase)
    return predicted_class

def getBestQuestion(question_utilisateur, juriclass="ent"):
    TfIdfQuestions_utilisateur = vectorizer.transform([question_utilisateur], True)


    # print("Question utilisateur = ",question_utilisateur)
    bestQuestionScore = None
    bestQuestionIndex = None
    for questionIndex in range (len(liste_questions)):
        #print("    Question: ",liste_questions[questionIndex])
        # Ici on vérifie que la classe du document est bien celle qu'on veut
        index_doc = "iris" + str(questionIndex + 1)
        if DOC_CLASS[documents_Corpus.get(index_doc)['class'].lower()] == juriclass:

            simScore = metrics.pairwise.cosine_similarity(TfIdfQuestions[questionIndex], TfIdfQuestions_utilisateur[0])
            #print ("        simScore: ",simScore)
            if not bestQuestionScore or simScore > bestQuestionScore:
                bestQuestionScore = simScore
                bestQuestionIndex = questionIndex

    # print("  ===> Best Question: ")
    if (bestQuestionIndex):
        index = "iris" + str(bestQuestionIndex)
        return documents_Corpus.get(index)
    else:
        return None

if False:
    question_utilisateur = input("Posez une question : ")
    assert(question_utilisateur != "")
    print("Votre question est : ", question_utilisateur)
    classe_question = predict(teampath+"/Groupes/interaction/flask-ChatLaw/model_class_question_uti", question_utilisateur)
    print("Classe:", classe_question)
