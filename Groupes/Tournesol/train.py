#!/bin/env python3

from getfeatures import features, getfeature
import tensorflow as tf
import xml.etree.ElementTree as ET
import numpy
numpy.set_printoptions(precision=2,threshold=1000,suppress=True)

##Avoir train corpus
print('Reading corpus and finding features')
xmlcorpus = ET.parse('../../Corpus/all-train.xml')
nodoc = 0

print('Création de la matrice numpy pour x et y')
docs = xmlcorpus.getroot().getchildren()
featurekeys = sorted(list(features.keys()))
x = numpy.zeros((len(docs), len(featurekeys)))
y = numpy.zeros((len(docs),2))

##la structure du label y : [0,1]= fake, [1,0]=trusted
print('Insertion des données dans la matrice')
for i in range(len(docs)):
    for j in range(len(featurekeys)):
        doc = docs[i]
        featurename = featurekeys[j]
        x[i,j] = getfeature(doc, featurename)
        fake = 0
        if doc.get('class') == 'fake':
            fake = 1
            y[i][1] = fake
        else :
            y[i][0] = 1
#print(x.shape)
#print(y.shape)

##fonction add_layer
def add_layer(inputs,in_size,out_size,activation_function=None):
    """
    Créer Weights et biases d'une façon aléatoire
    Return le résultat d'équation : Wx + b
    """
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    biases = tf.Variable(tf.zeros([1,out_size]) + 0.1) 
    Wx_plus_b = tf.matmul(inputs,Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

##fonction pour calculer accuracy
def compute_accuracy(v_xs,v_ys):
    """
    entrée = v_xs : données de test, v_ys :label de données de test
    return l'accuracy
    """
    global prediction
    y_pre = sess.run(prediction,feed_dict={xs:v_xs})
    
    #comparéer l'index de l'argument max de label Y et celui de prédiction
    correct_prediction = tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    result = sess.run(accuracy,feed_dict={xs:v_xs,ys:v_ys})
    return result


##placeholder
xs = tf.placeholder(tf.float32,[None,len(featurekeys)])
ys = tf.placeholder(tf.float32,[None,2])


##première couche
l1 = add_layer(xs,len(featurekeys),10,activation_function=tf.nn.softmax)

##deuxième couche
prediction = add_layer(l1,10,2,activation_function=tf.nn.softmax)
#softmax pour faire la classification
# le résutalt est la possibilité d'être fake ou truste, par exemple : [0.29 0.71] veut dire, 
# 29% possibilité être trusted, alors que 71% possibilité être fake.

##cross_entropy =loss
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),
                    reduction_indices=[1]))


##train
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(2000):
        sess.run(train_step,feed_dict={xs:x,ys:y})
    #print l'accuracy tous les 100 fois:
        if i % 100 == 0:
            print("l'accuracy est ", compute_accuracy(x,y))