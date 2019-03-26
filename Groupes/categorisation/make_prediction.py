# Functions to make class predictions,

# See also :
# test_make_prediction for a demo of calling these functions.

# Caution :
# By default, using the model trained with lemme+pos, if you'd like to try a
# model trained with lemme, try uncomment commented instructions in
# make_prediction

from sklearn.externals import joblib
from corpus import *

def load_model(path_to_model_file):
    """Loads the model.

    To see details of the model, you can type :
        print(model.classes_)
        print(model.get_params)

    Args:
        path_to_model_file: path to the saved model

    Returns:
        a model object

    """
    with open(path_to_model_file, 'rb') as model_handle:
        model = joblib.load(model_handle)
    return model

def make_prediction(model, phrase):
    """Predicts a phrase's class.

    Args:
        model: the model object returned by load_model
        phrase (str): a question to predicate its class

    Returns:
        the predicted class_(str)

    """
    qa = JurQA()
    qa.question.init_text(phrase)

    # if the model is trained with lemme+pos features, you need to call this
    predicted_class = model.predict([get_lp(qa)])

    # if the model is trained with lemme features, you need to uncomment this
    # predicted_class = model.predict(get_lemma(qa))

    return str(predicted_class[0])

def get_lemma(doc):
    """Returns lemme as features
    if the model is trained with lemme features, you need to call this
    """

    return " ".join(doc.question.lemma)

def get_lp(doc):
    """Returns lemme/pos as features
    if the model is trained with lemme+pos features, you need to call this
    """

    return " ".join([t[1]+"/"+t[2] for t in doc.question.tagged_text()])
