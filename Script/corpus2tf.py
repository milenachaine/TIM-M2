#!/bin/env python3

import xml.etree.ElementTree as ET
import numpy
numpy.set_printoptions(precision=2,threshold=1000,suppress=True)
from getfeatures import features, getfeature
import matplotlib.pyplot as plt
import tensorflow as tf

print('Reading corpus and finding features')
xmlcorpus = ET.parse('../Corpus/all.xml')
nodoc = 0

print('Création de la matrice numpy pour x et y')
docs = xmlcorpus.getroot().getchildren()
featurekeys = sorted(list(features.keys()))
x = numpy.zeros((len(docs), len(featurekeys)))
y = numpy.zeros((len(docs), 1))

print('Insertion des données dans la matrice')
for i in range(len(docs)):
	for j in range(len(featurekeys)):
		doc = docs[i]
		featurename = featurekeys[j]
		x[i,j] = getfeature(doc, featurename)
		fake = 0
		if doc.get('class') == 'fake':
			fake = 1
		y[i,0] = fake

print('Dimensions de la matrice des features: '+str(x.shape))

tfx = tf.placeholder(tf.float32, [None, len(featurekeys)])
tfy_ = tf.placeholder(tf.float32, [None, 1])

tfb = tf.Variable(tf.zeros([1]))
tfw = tf.Variable(tf.zeros([1,len(featurekeys)]))

tfy = tf.multiply(tfx, tfw) + tfb

loss = tf.reduce_sum((tfy - tfy_) * (tfy - tfy_))
train_step = tf.train.GradientDescentOptimizer(0.005).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10):
	sess.run(train_step, feed_dict={tfx:x,tfy_:y})
	print(step, sess.run(tfw), sess.run(tfb))

classification = sess.run(tfy, feed_dict={tfx: x})
print(classification)
