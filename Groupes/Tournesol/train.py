#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Jielei Li - Mingqiang Wang - Arthur Provenier

    Entrainement du modèle
"""

from __future__ import division
import os, argparse
from lxml import etree

import tensorflow as tf
import numpy as np

from get_features import getfeature
from get_tfidf import get_tfidf


parser = argparse.ArgumentParser()
parser.add_argument("input", help="Le jeu de données d'entrainement")
args = parser.parse_args()

# Les mots avec avec le tf-idf le plus élevé (à l'exception de 'de')
features = {f : 'numeric' for f in get_tfidf('../Corpus//all.xml')}

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
#trainX, trainY = make_matrices("corpus/all-train.xml")
trainX, trainY = make_matrices(args.input)
testX, testY = make_matrices("../Corpus/all-test.xml")


numFeatures = trainX.shape[1]
numLabels = trainY.shape[1]

numEpochs = 27000
learningRate = tf.train.exponential_decay(learning_rate=0.0008,
                                          global_step=1,
                                          decay_steps=trainX.shape[0],
                                          decay_rate=1,
                                          staircase=True)


X = tf.placeholder(tf.float32, [None, numFeatures])
yGold = tf.placeholder(tf.float32, [None, numLabels])


weights = tf.Variable(tf.random_normal([numFeatures,numLabels],
                                       mean=0,
                                       stddev=0.5,
                                       name="weights"))

bias = tf.Variable(tf.random_normal([1,numLabels],
                                    mean=0,
                                    stddev=2,
                                    name="bias"))


init_OP = tf.global_variables_initializer()


apply_weights_OP = tf.matmul(X, weights, name="apply_weights")
add_bias_OP = tf.add(apply_weights_OP, bias, name="add_bias")
activation_OP = tf.nn.sigmoid(add_bias_OP, name="activation")


cost_OP = tf.nn.l2_loss(activation_OP-yGold, name="squared_error_cost")


training_OP = tf.train.GradientDescentOptimizer(learningRate).minimize(cost_OP)


sess = tf.Session()
sess.run(init_OP)


correct_predictions_OP = tf.equal(tf.argmax(activation_OP,1),tf.argmax(yGold,1))
accuracy_OP = tf.reduce_mean(tf.cast(correct_predictions_OP, tf.float32))


# Initialize reporting variables
cost = 0
diff = 1


# Create Saver
saver = tf.train.Saver()

# Training epochs
for i in range(numEpochs):
    if i > 1 and diff < .0001:
        #print("change in cost %g; convergence."%diff)
        break
    else:
        # Run training step
        step = sess.run(training_OP, feed_dict={X: trainX, yGold: trainY})
        # Report occasional stats
        if i % 10 == 0:
            # Generate accuracy stats on test data
            train_accuracy, newCost = sess.run(
                [accuracy_OP, cost_OP],
                feed_dict={X: trainX, yGold: trainY}
            )

            # Re-assign values for variables
            diff = abs(newCost - cost)
            cost = newCost

            #generate print statements
            #print("step %d, training accuracy %g"%(i, train_accuracy))
            #print("step %d, cost %g"%(i, newCost))
            #print("step %d, change in cost %g"%(i, diff))

'''
print("[Train] Précision sur le jeu de test : {}".format(sess.run(accuracy_OP,
                                                        feed_dict={X: testX,
                                                        yGold: testY})))
'''

# Save variables to .ckpt file
saver.save(sess, "./model")

# Close tensorflow session
sess.close()
