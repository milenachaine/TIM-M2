#!usr/bin/env python3
#coding: utf-8

import sys
import time
import argparse
from nltk import wordpunct_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string
import tensorflow as tf
import numpy as np
import xml.etree.ElementTree as ET
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer

# parser des arguments: fichier de test, modèle, fichier de sortie (en xml)
aparser = argparse.ArgumentParser(description='Use model for prediction')
aparser.add_argument('input', help='Input file')
aparser.add_argument('model', help='Model file')
aparser.add_argument('test', help='Test file')
aparser.add_argument('output', help='Output file')
args = aparser.parse_args()
print('Reading corpus and finding features')
xmlcorpus = ET.parse(args.test)
docs = xmlcorpus.getroot().getchildren()


# on fait des même prétraitements pour des données de test.
def corpus_extraction(path):
    print('Reading corpus and finding features')
    xmlcorpus = ET.parse(path)
    textes = xmlcorpus.findall('.//text')
    tags_corpus = xmlcorpus.findall('.//treetagger')
    corpus = []
    tags = []
    for i in textes:
        corpus.append(i.text)
    for i in tags_corpus:
        tags.append(i.text)
    # les étiquettes du document (références)
    docs= xmlcorpus.getroot().getchildren()
    Y = np.zeros((len(docs), 3))
    for i in range(len(docs)):
        doc = docs[i]
        fake = 0
        if doc.get('class') == 'fake':
            Y[i,0] = 1
        elif doc.get('class') == "parodic":
            Y[i,1] = 1
        else:
            Y[i,2] = 1
    return corpus,tags,Y




train_corpus,train_tags, train_Y = corpus_extraction(args.input)
test_corpus,test_tags, test_Y = corpus_extraction(args.test)


def preprocessing_corpus(corpus):
    processed_corpus = []
    stemmer = PorterStemmer()
    for sample in corpus:
        sample = sample.replace('\n','')
        s = ''
        for word in wordpunct_tokenize(sample):
            if word and word.lower() not in stopwords.words('french'):
                s =s + stemmer.stem(word.lower()) + ' '
        processed_corpus.append(s)
    return processed_corpus

train_corpus = preprocessing_corpus(train_corpus)
test_corpus = preprocessing_corpus(test_corpus)

train_tags = preprocessing_corpus(train_tags)
test_tags = preprocessing_corpus(test_tags)

tfidf_corpus = TfidfVectorizer()
tfidf_corpus.fit_transform(train_corpus+test_corpus)
train_corpus_feature = tfidf_corpus.transform(train_corpus).toarray()
test_corpus_feature = tfidf_corpus.transform(test_corpus).toarray()

tfidf_tags = TfidfVectorizer()
tfidf_tags.fit_transform(train_tags+test_tags)
train_tags_feature = tfidf_tags.transform(train_tags).toarray()
test_tags_feature = tfidf_tags.transform(test_tags).toarray()

# importation des modèles
saver = tf.train.import_meta_graph(args.model+"/model.ckpt.meta")
# initiation de session
sess = tf.Session()
# restauration des paramètres à partir du chekpoint
saver.restore(sess, args.model+"/model.ckpt") 

all_vars = tf.get_collection('vars')
X = all_vars[0]
Y = all_vars[1]
weights = all_vars[2]
bias = all_vars[3]

# redéfinition des calculs des paramètres
apply_weights_OP = tf.matmul(X, weights, name="apply_weights")
add_bias_OP = tf.add(apply_weights_OP, bias, name="add_bias")
activation_OP = tf.nn.softmax(add_bias_OP, name="activation")
cost_OP = tf.nn.l2_loss(activation_OP-Y, name="squared_error_cost")
correct_predictions_OP = tf.equal(tf.argmax(activation_OP,1),tf.argmax(Y,1))
accuracy_OP = tf.reduce_mean(name="accuracy_OP",input_tensor=tf.cast(correct_predictions_OP, "float"))

print("final accuracy on test set: %s£" %str(sess.run(accuracy_OP, feed_dict={X: test_tags_feature, Y: test_Y})))

predictions = sess.run(activation_OP, feed_dict={X: test_tags_feature})
predict = sess.run(tf.argmax(predictions,1))
print(len(predict))
print(len(docs))

# écrit le résultat de prédiction dans le fichier de sortie
for i in range(0, len(docs)):
    classpredict = ''
    if predict[i] == 0:
        classpredict = 'fake'
    if predict[i] == 1:
        classpredict = 'parodic'
    if predict[i] == 2:
        classpredict = 'trusted'
    docs[i].set('classpredict', classpredict)
xmlcorpus.write(open(args.output, 'wb'), encoding='UTF-8')


