"""Categorisation des documents.

    Test a model trained with 500 tfidf features and random forest classifier.

    USAGE : python3 test_model.py <PATH_TO_MODEL>
"""
import test_data_user
import sys
from sklearn.externals import joblib

def main():
    # Load model
    with open(sys.argv[1], "rb") as m_handle:
        rfc_model = joblib.load(m_handle)

    # Prepare test data
    # test (list)
    #test = test_data_user.questions

    # Make prediction
    question = open(sys.argv[2], "r").read()
    pred = rfc_model.predict(question)

    return pred

if __name__ == "__main__":
    main()
