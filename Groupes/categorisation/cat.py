"""categorisation des documents

    Classifier les documents provenant du forum juridique en 8 classes
"""
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys

from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

FEATURE_SIZE = 500
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

def main():
    # prepare data
    tree = ET.ElementTree(file=sys.argv[1])
    X = list()
    Y = list()
    for doc in tree.getroot():
        question = " ".join([q.text.strip() for q in doc.findall("question")])
        Y.append(DOC_CLASS[doc.get("class").lower()])
        X.append(question)

    # train_test protocol: 8:2
    x_train, x_test, y_train, y_test = \
        train_test_split(X, Y, test_size=0.2, random_state=12)

    # pipeline
    rf = RandomForestClassifier()
    vectorizer = TfidfVectorizer(max_features=FEATURE_SIZE)
    pipeline = Pipeline([
        ('tfidf', vectorizer),
        ('rf', rf)
    ])

    # parameter tuning
    parameters = {
        "rf__n_estimators": [20,40,60,80,100,],
        "rf__oob_score": [True,],
        "rf__random_state": [10,]
    }
    tfidf_rf_clf = GridSearchCV(pipeline,parameters)
    tfidf_rf_clf.fit(x_train,y_train)
    print("BEST SCORE: ",tfidf_rf_clf.best_score_)
    print("BEST PARAMETERS: ", tfidf_rf_clf.best_params_)
    y_pred = tfidf_rf_clf.predict(x_test)
    class_names = DOC_CLASS.values()
    # evaluation
    print(metrics.classification_report(y_test, y_pred,
                                     target_names=class_names))


    # save pipeline
    joblib.dump(tfidf_rf_clf, "tfidf_rf_clf")

    # create arff
    # features = vectorizer.get_feature_names()
    # sets = {
    #     'x_train': x_train,
    #     'x_test': x_test,
    #     'y_train': y_train,
    #     'y_test': y_test
    # }
    # corpus2arff(features,**sets)

def corpus2arff(features,x_train,x_test,y_train,y_test):
    with open("train.arff", "w", encoding="utf-8") as TRAIN, \
            open("test.arff","w", encoding="utf-8") as TEST:
        TRAIN.write("@RELATION juritique\n")
        for f in features:
            TRAIN.write("@ATTRIBUTE "+f+"\tNUMERIC\n")
        TRAIN.write(
            "@ATTRIBUTE class\t{{{0}}}\n".format(", ".join(DOC_CLASS.values()))
        )
        TRAIN.write("@DATA\n")
        for i in range(x_train.shape[0]):
            TRAIN.write(", ".join(str(j) for j in x_train[i]))
            TRAIN.write(", "+y_train[i]+"\n")

        TEST.write("@RELATION juritique\n")
        for f in features:
            TEST.write("@ATTRIBUTE " + f + "\tNUMERIC\n")
        TEST.write(
            "@ATTRIBUTE class\t{{{0}}}\n".format(", ".join(DOC_CLASS.values()))
        )
        TEST.write("@DATA\n")
        for i in range(x_test.shape[0]):
            TEST.write(", ".join(str(j) for j in x_test[i]))
            TEST.write(", "+y_test[i]+"\n")



if __name__ == "__main__":
    main()
