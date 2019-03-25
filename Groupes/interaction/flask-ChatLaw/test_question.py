import pickle

relpath = '../Similarite/'
documents_Corpus = pickle.load(open(relpath+"documents_Corpus.pkl", "rb"))
vectorizer = pickle.load(open(relpath+"vectorizer.pkl", "rb"))
TfIdfQuestions = pickle.load(open(relpath+"TfIdfQuestions.pkl", "rb"))
liste_questions = pickle.load(open(relpath+"liste_questions.pkl", "rb"))

question_utilisateur = "J'ai des factures impayées"
TfIdfQuestions_utilisateur = vectorizer.transform([question_utilisateur], True)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics, feature_extraction

print("Question utilisateur = ",question_utilisateur)
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

print("  ===> Best Question: ")
if (bestQuestionIndex):
    index = "iris" + str(bestQuestionIndex)
    print("       QuestionIndex: ",bestQuestionIndex," => ", documents_Corpus.get(index))
    
