# -*- coding: UTF-8 -*-
import pickle

path = '/home/teamlaw/git-TIM-M2/Groupes/Similarite/'
# path = '../../Similarite/'
documents_Corpus = pickle.load(open(path+"documents_Corpus.pkl", "rb"))
vectorizer = pickle.load(open(path+"vectorizer.pkl", "rb"))
TfIdfQuestions = pickle.load(open(path+"TfIdfQuestions.pkl", "rb"))
liste_questions = pickle.load(open(path+"liste_questions.pkl", "rb"))

def getBestQuestion(question_utilisateur):
    TfIdfQuestions_utilisateur = vectorizer.transform([question_utilisateur], True)

    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn import metrics, feature_extraction

    # print("Question utilisateur = ",question_utilisateur)
    bestQuestionScore = None
    bestQuestionIndex = None
    for questionIndex in range (len(liste_questions)):
        #print("    Question: ",liste_questions[questionIndex])
        # Ici on vérifie que la classe du document est bien celle qu'on veut
        index_doc = "iris" + str(questionIndex + 1)
        if documents_Corpus.get(index_doc)['class'] == "Entreprise":

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
        
print(getBestQuestion("J'ai des factures impayées"))
