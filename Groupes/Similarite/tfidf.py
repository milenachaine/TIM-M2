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
question_utilisateur = ['Je veux annuler une caution solidaire']

doc_q = open("doc_q.txt", "w")
qs = ""
for q in question_utilisateur:
    qs+=q
doc_q.write(qs)


print(qs)

commande = "python3 test_model_user.py " + "model_class_question_uti " + "doc_q.txt"
print("Commande ", commande)
classe_question = os.system(commande)
print("classe question", classe_question)
"""

def lireDocs():
    docs = {}

    fichier_tree = ET.parse("corpusIrisVersion4.xml")
    fichier_docs = fichier_tree.getroot()
    compteur_docs = 0

    for document in fichier_docs:
        compteur_docs += 1
        doc_id = document.attrib['id']
        questions = ''
        answers = ''
        doc_class = document.attrib['class']
        doc_subclass = document.attrib['subclass']
        for child in document:
            if child.tag == 'question':
                questions += child.text.rstrip()

            if child.tag == 'answer':
                answers += child.text.rstrip()

        doc = {}
        doc['id']= doc_id
        doc['class'] = doc_class
        doc['subclass'] = doc_subclass
        doc['questions'] = questions
        doc['answers'] = answers
        docs[doc_id] = doc

    print("Total docs : ", compteur_docs)

    return docs

documents_Corpus = lireDocs()

def preprocessingDocs(documents):
    print("Preprocessing documents")
    for element in documents:
        document = documents[element]

        # Suppression de signes de ponctuation avec tokenizer
        questions = document['questions']
        q_words = ' '.join(tokenizer.tokenize(questions))
        document['words_questions'] = q_words
        answers = document['answers']
        aw_words = ' '.join(tokenizer.tokenize(answers))
        document['words_answers'] = aw_words

    mots = [[]]
    for element in documents:
        document = documents[element]
        q_texte = document['words_questions']
        questionPreprocess = []

        for mot in tokenizer.tokenize(q_texte):
            if mot.lower() not in stopWords:
                mot_stem = stemmer.stem(mot.lower())
                questionPreprocess.append(mot_stem)
                mots.append([(mot_stem)])
        document['words_questions'] = ' '.join(questionPreprocess)

        aw_texte = document['words_answers']
        answerPreprocess = []

        for mot in tokenizer.tokenize(aw_texte):
            if mot.lower() not in stopWords:
                mot_stem = stemmer.stem(mot.lower())
                answerPreprocess.append(mot_stem)

        document['words_answers'] = ' '.join(answerPreprocess)

    return mots

mots_questions_Corpus = preprocessingDocs(documents_Corpus)

def getWordsQuestions(documents):
    liste_questions_stems = []
    for element in documents:
        document = documents[element]
        liste_questions_stems.append(document['words_questions'])
    return liste_questions_stems

liste_questions = getWordsQuestions(documents_Corpus)

vectorizer = TfidfVectorizer()
TfIdfQuestions = vectorizer.fit_transform(liste_questions)
TfIdfQuestions_utilisateur = vectorizer.transform(question_utilisateur, True)



for question_utilisateurIndex in range (len(question_utilisateur)):
    print("Question utilisateur = ",question_utilisateur[question_utilisateurIndex])

    bestQuestionScore = None
    bestQuestionIndex = None

    for questionIndex in range (len(liste_questions)):

        #print("    Question: ",liste_questions[questionIndex])

        simScore = metrics.pairwise.cosine_similarity(TfIdfQuestions[questionIndex], TfIdfQuestions_utilisateur[question_utilisateurIndex])
        #print ("        simScore: ",simScore)
        if not bestQuestionScore or simScore > bestQuestionScore:
            bestQuestionScore = simScore
            bestQuestionIndex = questionIndex

    print("  ===> Best Question: ")
    if (bestQuestionIndex):
        index = "iris" + str(bestQuestionIndex)

        print("       QuestionIndex: ",bestQuestionIndex," => ", documents_Corpus.get(index))
"""
