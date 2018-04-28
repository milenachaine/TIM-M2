#!/bin/python3
#coding : utf8

"""Exemple de DNN à partir de l'exemple
https://www.tensorflow.org/get_started/get_started_for_beginners
"""
import tensorflow as tf
import prepare_data

BATCH_SIZE = 100
TRAIN_STEPS = 1000

def main():

    # Modifier le chemin!
    (train_x, train_y) = prepare_data.load_data("../Corpus/all-train.xml")
    (test_x, test_y) = prepare_data.load_data("../Corpus/all-test.xml")

    # Feature columns describe how to use the input.
    my_feature_columns = []
    for key in train_x.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    # Build 2 hidden layer DNN with 10, 10 units respectively.
    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        # Two hidden layers of 10 nodes each.
        hidden_units=[10, 10],
        # The model must choose between 3 classes.
        n_classes=3)

    # Train the Model.
    classifier.train(
        input_fn=lambda:prepare_data.train_input_fn(train_x, train_y,
                                                 BATCH_SIZE),
        steps=TRAIN_STEPS)

    # Evaluate the model.
    eval_result = classifier.evaluate(
        input_fn=lambda:prepare_data.eval_input_fn(test_x, test_y,
                                                BATCH_SIZE))

    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))


if __name__ == '__main__':
    main()
