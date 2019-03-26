# DEMO : how to make prediction for a sentence given by using functions
# built in make_prediction.py

# Caution :
# by default, using the model trained with lemme+pos, if you'd
# like to try a model trained with lemme, try commented instructions in
# make_prediction in make_rediction.py

# USAGE :
# python3 test_make_prediction.py <path_to_saved_model> <one_sent_to_predict>

import sys
from make_prediction import *

def main():

    path_to_model = sys.argv[1]
    phrase_to_predict = sys.argv[2]

    # load the model in memory with the function load_model
    # you only need to load the model once (if you don't intend to change
    # another model)
    model = load_model(path_to_model)

    # make prediction for a phrase with the funciton make_prediction
    # can loop this for more predictions
    predicted_class = make_prediction(model, phrase_to_predict)

    print(predicted_class)


if __name__ == '__main__':
    main()