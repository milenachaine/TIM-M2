#!/bin/env python3

import xml.etree.ElementTree as ET
import numpy as np
np.set_printoptions(precision=2,threshold=1000,suppress=True)
from getfeatures import features, getfeature
import matplotlib.pyplot as plt
import tensorflow as tf

print('Reading corpus and finding features')
xmlcorpus = ET.parse('../Corpus/all.xml')
nodoc = 0

print('Création de la matrice numpy pour x et y')
docs = xmlcorpus.getroot().getchildren()
featurekeys = sorted(list(features.keys()))
trainX = np.zeros((len(docs), len(featurekeys)))
trainY = np.zeros((len(docs), 1))

print('Insertion des données dans la matrice')
for i in range(len(docs)):
	for j in range(len(featurekeys)):
		doc = docs[i]
		featurename = featurekeys[j]
		trainX[i,j] = getfeature(doc, featurename)
		fake = 0
		if doc.get('class') == 'fake':
			fake = 1
		trainY[i,0] = fake

print('Dimensions de la matrice des features: '+str(trainX.shape))

numFeatures = trainX.shape[1]
numLabels = trainY.shape[1]
numEpochs = 100
learningRate = tf.train.exponential_decay(learning_rate=0.0001, global_step= 1, decay_steps=trainX.shape[0], decay_rate= 0.95)
X = tf.placeholder(tf.float32, [None, numFeatures])
yGold = tf.placeholder(tf.float32, [None, numLabels])
weights = tf.Variable(tf.random_normal([numFeatures,numLabels]))
bias = tf.Variable(tf.random_normal([1,numLabels]))
init_OP = tf.initialize_all_variables()
apply_weights_OP = tf.matmul(X, weights)
add_bias_OP = tf.add(apply_weights_OP, bias) 
activation_OP = tf.nn.sigmoid(add_bias_OP)
cost_OP = tf.nn.l2_loss(activation_OP-yGold)
training_OP = tf.train.GradientDescentOptimizer(learningRate).minimize(cost_OP)
sess = tf.Session()
sess.run(init_OP)
correct_predictions_OP = tf.equal(tf.argmax(activation_OP,1),tf.argmax(yGold,1))
accuracy_OP = tf.reduce_mean(tf.cast(correct_predictions_OP, "float"))
activation_summary_OP = tf.summary.histogram("output", activation_OP)
accuracy_summary_OP = tf.summary.scalar("accuracy", accuracy_OP)
cost_summary_OP = tf.summary.scalar("cost", cost_OP)
weightSummary = tf.summary.histogram("weights", weights.eval(session=sess))
biasSummary = tf.summary.histogram("biases", bias.eval(session=sess))
all_summary_OPS = tf.summary.merge_all()
cost = 0
diff = 1
for i in range(numEpochs):
    if i > 1 and diff < .0001:
        print("change in cost %g; convergence."%diff)
        break
    else:
        step = sess.run(training_OP, feed_dict={X: trainX, yGold: trainY})
        if i % 10 == 0:
            results, accuracy, newCost = sess.run([all_summary_OPS, accuracy_OP, cost_OP], feed_dict={X: trainX, yGold: trainY})
            diff = abs(newCost - cost)
            cost = newCost
            print("step %d, training accuracy %g"%(i, accuracy))
            print("step %d, cost %g"%(i, newCost))
            print("step %d, change in cost %g"%(i, diff))
print("final accuracy on test set: %s" %str(sess.run(accuracy_OP, feed_dict={X: trainX, yGold: trainY})))
