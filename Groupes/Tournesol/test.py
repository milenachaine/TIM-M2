#!/bin/env python3

from getfeatures import features, getfeature
import tensorflow as tf
import xml.etree.ElementTree as ET
import numpy
from train.py import add_layer,compute_accuracy
numpy.set_printoptions(precision=2,threshold=1000,suppress=True)

##Avoir test corpus
print('Reading corpus and finding features')
xmlcorpus = ET.parse('../../Corpus/all-test.xml')
nodoc = 0

print('Création de la matrice numpy pour x et y')
docs = xmlcorpus.getroot().getchildren()

x2 = numpy.zeros((len(docs), len(featurekeys)))
y2 = numpy.zeros((len(docs),2))

print('Insertion des données dans la matrice')
for i in range(len(docs)):
    for j in range(len(featurekeys)):
        doc = docs[i]
        featurename = featurekeys[j]
        x2[i,j] = getfeature(doc, featurename)
        fake = 0
        if doc.get('class') == 'fake':
            fake = 1
            y2[i][1] = fake
        else :
            y2[i][0] = 1
#print(x2.shape)
#print(y2.shape)


## Pour Jielei à Modifier !!
def output(v_xs,v_ys):
    # return un fichier xml pour stcoker la prédiction
    global prediction
    y_pre = sess.run(prediction,feed_dict={xs:v_xs})
    with open('output.xml','w') as file:
        file.write('xml\n')
        for i in y_pre:
            if i[0] <= 0.50:
                file.write('truste\n')
            else :
                file.write('fake\n')
    return None


l1 = add_layer(xs,len(featurekeys),10,activation_function=tf.nn.softmax)
prediction = add_layer(l1,10,2,activation_function=tf.nn.softmax)
#softmax pour faire la classification
# le résutalt est la possibilité d'être fake ou truste, par exemple : [0.29 0.71] veut dire, 
# 29% possibilité être trusted, alors que 71% possibilité être fake.

cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),
                    reduction_indices=[1]))#cross_entropy =loss

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)
init=tf.global_variables_initializer()

#train
with tf.Session() as sess:
    sess.run(init)
    for i in range(2000):
        sess.run(train_step,feed_dict={xs:x,ys:y})
    
    #print l'accuracy tous les 100 fois:
        if i % 100 == 0:
            print("l'accuracy est ", compute_accuracy(x2,y2))