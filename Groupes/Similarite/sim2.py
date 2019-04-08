import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics, feature_extraction

answers = pickle.load(open("answers.pkl", "rb"))
answers_normalized = pickle.load(open("answers_normalized.pkl", "rb"))
question_uti_normalize = pickle.load(open("question_uti_normalized.pkl", "rb"))

vectorizer_answers = TfidfVectorizer()
TfIdfAnswers = vectorizer_answers.fit_transform(answers_normalized)

TfIdfCompareQuestionAnswer = vectorizer_answers.transform([question_uti_normalize], True)


bestAnswerScore = None
bestAnswerIndex = None

for AnswerIndex in range(len(answers)):
    simScore = metrics.pairwise.cosine_similarity(TfIdfAnswers[AnswerIndex], TfIdfCompareQuestionAnswer[0])
    #print("SimScore : ", simScore)
    if not bestAnswerScore or simScore > bestAnswerScore:

        bestAnswerIndex = AnswerIndex
        bestAnswerScore = simScore



if bestAnswerScore:
    print("Best answer score : {0} \n Best answer : {1}\n".format(bestAnswerIndex, answers[bestAnswerIndex]))
