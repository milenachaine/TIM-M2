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

FEATURE_SIZE = 1000
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
    parameters = {
        "n_estimators": 100,
        "oob_score": True,
        "random_state": 10,
    }
    rf = RandomForestClassifier(**parameters)
    vectorizer = TfidfVectorizer(max_features=FEATURE_SIZE)
    tfidf_rf_clf = Pipeline([
        ('tfidf', vectorizer),
        ('rf', rf)
    ])

    # TODO parameter tuning GridSearchCV
    # tfidf_rf_clf = GridSearchCV(pipeline,parameters)

    tfidf_rf_clf.fit(x_train,y_train)
    y_pred = tfidf_rf_clf.predict(x_test)
    class_names = DOC_CLASS.values()
    # evaluation
    print(metrics.classification_report(y_test, y_pred,
                                     target_names=class_names))

    # save pipeline
    joblib.dump(tfidf_rf_clf, "tfidf_rf_clf")

if __name__ == "__main__":
    main()
