#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Jielei Li - Mingqiang Wang - Arthur Provenier

    Prédiction de labels
"""

from __future__ import division
import os, argparse
from lxml import etree

import tensorflow as tf
import numpy as np

from get_features import getfeature
from get_tfidf import get_tfidf

parser = argparse.ArgumentParser()
parser.add_argument("test", help="Le jeu de test")
parser.add_argument("model", help="Le chemin vers le modèle")
parser.add_argument("output", help="La sortie xml")
args = parser.parse_args()


# Les mots avec avec le tf-idf le plus élevé (à l'exception de 'de')
features = {f : 'numeric' for f in get_tfidf('../Corpus/all.xml')}

# Features perso
features.update({
                'selon': 'numeric',
                'on': 'numeric',
                'nous' : 'numeric',
                '«' : 'numeric',
                '»' : 'numeric',
                '?' : 'numeric',
                ',' : 'numeric',
                ':' : 'numeric'
                })

# Nom des features trié
FEATURE_KEYS = sorted(list(features.keys()))
LABELS = ["fake", "trusted", "parodic"]


# Pour une initialisation déterministe
tf.set_random_seed(12)


def make_matrices(corpus):
    """Création des matrices
        x : matrice des features
        y : matrice des labels"""


    with open(corpus, encoding="utf-8") as f:
        tree = etree.parse(f)

    document_label = [doc.get("class") for doc in tree.xpath("//doc")]

    x = np.zeros((len(document_label), len(FEATURE_KEYS)))
    y = np.zeros((len(document_label), len(LABELS)))

    for i, doc in enumerate(tree.xpath("//text")):
        doc = doc.text
        for j, feature in enumerate(FEATURE_KEYS):
            x[i,j] = getfeature(doc, feature)

        if document_label[i] == 'fake':
            y[i][0] = 1
        elif document_label[i] == 'trusted':
            y[i][1] = 1
        else:
            y[i][2] = 1

    return (x, y)


# Création des jeux de données
trainX, trainY = make_matrices("../Corpus/all-train.xml")
testX, testY = make_matrices(args.test)


numFeatures = trainX.shape[1]   # Nombre de features
numLabels = trainY.shape[1]     # Nombre de labels (ici 3)


sess = tf.Session()


X = tf.placeholder(tf.float32, [None, numFeatures])
yGold = tf.placeholder(tf.float32, [None, numLabels])


weights = tf.Variable(tf.zeros([numFeatures,numLabels]))
bias = tf.Variable(tf.zeros([1,numLabels]))


apply_weights_OP = tf.matmul(X, weights, name="apply_weights")
add_bias_OP = tf.add(apply_weights_OP, bias, name="add_bias")
activation_OP = tf.nn.sigmoid(add_bias_OP, name="activation")


correct_predictions_OP = tf.equal(tf.argmax(activation_OP,1),tf.argmax(yGold,1))
accuracy_OP = tf.reduce_mean(tf.cast(correct_predictions_OP, "float"))


init_OP = tf.global_variables_initializer()

sess.run(init_OP)

# Charger le modèle depuis
saver = tf.train.Saver()
saver.restore(sess, './' + args.model)


def labelToString(label):
    labels = ["fake", "trusted", "parodic"]

    return labels[np.argmax(label)]


if __name__ == "__main__":

    #show predictions and accuracy of entire test set
    prediction, evaluation = sess.run([activation_OP, accuracy_OP], feed_dict={X: testX, yGold: testY})

    y_true = []
    y_pred = []

    for i in range(len(testX)):
        y_true.append(labelToString(testY[i]))      # Vrai label
        y_pred.append(labelToString(prediction[i])) # Label prédit
    print("[Test] Précision sur l'ensemble du jeu de test : {}".format(evaluation))

    with open(args.test, 'r', encoding="utf-8") as f:
        tree = etree.parse(f)
        for i, doc in enumerate(tree.xpath("//doc")):
            doc.set('classpredict', y_pred[i])
        tree.write(open(args.output, 'wb'), encoding="utf-8", xml_declaration=True)


    # Pour la matrice de confusion
    '''
    from sklearn.metrics import confusion_matrix
    import itertools
    import matplotlib.pyplot as plt

    def plot_confusion_matrix(cm, classes,
                              normalize=False,
                              title='Confusion matrix',
                              cmap=plt.cm.Blues):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")
        else:
            print('Confusion matrix, without normalization')

        print(cm)

        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')

    # Compute confusion matrix
    cnf_matrix = confusion_matrix(y_true, y_pred)
    np.set_printoptions(precision=2)
    plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=LABELS, normalize=True,
                          title='Normalized confusion matrix')

    plt.show()
    '''
