import sys
from sklearn.externals import joblib
from corpus import *

def main():
    with open(sys.argv[1],"rb") as FI:
        model = joblib.load(FI)
        qa = JurQA()
        qa.question.init_text(sys.argv[2])
        result = model.predict([get_lp(qa)])
        print(result)


def get_lemma(doc):
    return " ".join(doc.question.lemma)

def get_lp(doc):
    return " ".join([t[1]+"/"+t[2] for t in doc.question.tagged_text()])

if __name__ == "__main__":
    main()