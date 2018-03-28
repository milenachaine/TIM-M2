#!/bin/python3
#coding : utf8

"""
    http://adventuresinmachinelearning.com/gensim-word2vec-tutorial/
    https://sourcedexter.com/tensorflow-text-classification-python/
"""
import PrepareCorpus as pc

import gensim
import numpy as np
import tflearn
import tensorflow as tf

# Modifier le chemin si nécessaire
corpus_train = pc.PreparationCorpus("../Corpus/all-train.xml")

#documents_class = corp.getDocumentsType()
documents = corpus_train.getDocuments()
documents_class = corpus_train.getDocumentsType()

mots_uniques = list(set([token for docs in documents for token in docs]))


docs = []
for classe, sent in zip(documents_class, documents):
    docs.append((sent, classe))

categories = list(set(documents_class)) # 3

# create our training data
training = np.zeros((len(documents), len(mots_uniques)))

labels = np.zeros((len(documents), len(categories)))

for i, doc in enumerate(docs):
    # list of tokenized words for the pattern
    token_words = doc[0]
    # create our bag of words array
    for y, w in enumerate(mots_uniques):
        if w in token_words:
            training[i,y] = 1
        else:
            training[i,y] = 0

    labels[i,categories.index(doc[1])] = 1

# reset underlying graph data
tf.reset_default_graph()
# Build neural network
input_data = tflearn.input_data(shape=[None, len(training[0])])
fc1 = tflearn.fully_connected(input_data, 64)
fc2 = tflearn.fully_connected(fc1, len(labels[0]), activation='softmax')
net = tflearn.regression(fc2)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# Start training (apply gradient descent algorithm)
epochs = 1000
model.fit(training, labels, n_epoch=epochs, batch_size=8, show_metric=True)

##################
## TEST
##################
corpus_test = pc.PreparationCorpus("../Corpus/all-test.xml")
documents_test = corpus_test.getDocuments()
documents_test_class = corpus_test.getDocumentsType()

resultat = 0
for y, sent in enumerate(documents_test):
    bow = [0] * len(mots_uniques)
    for mot in sent:
        for i, w in enumerate(mots_uniques):
            if w == mot:
                bow[i] = 1
    bow = np.array(bow)

    prediction = categories[np.argmax(model.predict([bow]))]
    label_gold = documents_test_class[y]

    res_str = "Prédiction : {} - Vrai : {}".format(prediction, label_gold)
    print(res_str)

    if prediction == label_gold:
        resultat += 1

print(resultat * 100 / len(documents_test_class))
# ~ 54 % de précision
