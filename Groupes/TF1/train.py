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

# fonction qui prend un chemin du fichier en entrée, qui renvoie une liste qui contient le contenu de corpus, une liste contient les les tokens, pos taggers et lemmes dans le corpus, et une matrice qui stoke pour chaque document sa classe de référence. 
def corpus_extraction(path):
    print('Reading corpus and finding features')
    xmlcorpus = ET.parse(path)
    textes = xmlcorpus.findall('.//text')
    tags_corpus = xmlcorpus.findall('.//treetagger')
    corpus = []
    tags = []
    for i in textes:
        # corpus contient le contenu du corpus
        corpus.append(i.text)
    for i in tags_corpus:
        # tags contient les taggers du corpus
        tags.append(i.text)
    # docs contient les étiquettes(références) du document
    docs = xmlcorpus.getroot().getchildren()
    # Y est une matrice, nb de ligne = nb de documents, nb de colonnes = 3 (nb de classes)
    Y = np.zeros((len(docs), 3))
    for i in range(len(docs)):
        doc = docs[i]
        fake = 0
        # dans la matrice Y, la première colonne est fake, la 2eme est parodic, la troisième est trusted 
        if doc.get('class') == 'fake':
            Y[i,0] = 1
        elif doc.get('class') == "parodic":
            Y[i,1] = 1
        else:
            Y[i,2] = 1
    return corpus,tags,Y


# appelle la fonction corpus_extraction et enregisiter les résultats pour le trainning set et pour le test set
aparser = argparse.ArgumentParser(description='Train model')
aparser.add_argument('input', help='Input file')
aparser.add_argument('model', help='Model file')
aparser.add_argument('test', help='Test file')
args = aparser.parse_args()
print(type(args.model))
train_corpus,train_tags, train_Y = corpus_extraction(args.input)
test_corpus,test_tags, test_Y = corpus_extraction(args.test)

# fonction qui prend le contenu du corpus(un training set stocké dans une liste) en entrée et renvoie une liste qui contient le corpus nettoyé
# prétraitelent réalisé : stemming, enlever les sautes lignes, enlever les stopwords
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


# appelle la fonction de prétraitement, entregistrer le résultat de trainning set et de test set
train_corpus = preprocessing_corpus(train_corpus)
test_corpus = preprocessing_corpus(test_corpus)
train_tags = preprocessing_corpus(train_tags)
test_tags = preprocessing_corpus(test_tags)

# initialiser TfidfVectorizer, convertit le corpus de train(contenus des documents) et le corpus de test(contenus des documents) en deux matrice, chaque matrice contient les features de tokens en valeur tfidf 
# le corpus en une matrice qui contient les tf-idf features 
tfidf_corpus = TfidfVectorizer()
tfidf_corpus.fit_transform(train_corpus+test_corpus)
# écrit les features dans la matrice 
train_corpus_feature = tfidf_corpus.transform(train_corpus).toarray()
test_corpus_feature = tfidf_corpus.transform(test_corpus).toarray()

# initialiser TfidfVectorizer, convertit le corpus de train(pos taggers pour tous les tokens) et le corpus de test(pos taggers pour tous les tokens) en deux matrice, chaque matrice contient les features de postaggers en valeur tfidf 
tfidf_tags = TfidfVectorizer()
tfidf_tags.fit_transform(train_tags+test_tags)
train_tags_feature = tfidf_tags.transform(train_tags).toarray()
test_tags_feature = tfidf_tags.transform(test_tags).toarray()

# la dimension de features -> nb d'input
feature_size = train_tags_feature.shape[1]
# nb de labels à prédire
label_size = train_Y.shape[1]
# la période pour traiter les données
numEpochs = 10000
# taux d'apprentissage
learningRate = tf.train.exponential_decay(learning_rate=0.008,
                                          global_step= 1,
                                          decay_steps=train_tags_feature.shape[0],
                                          decay_rate= 0.95,
                                          staircase=True)
# X est une matrice, le nb de ligne n'est pas fixé, le bombre de colonnes est le nb de feautres
X = tf.placeholder(tf.float32,[None,feature_size],name="X")
# Y est une matrice, le nb de ligne n'est pas fixé, le bombre de colonnes est le nb de classes à prédire=3
Y = tf.placeholder(tf.float32,[None,label_size],name = "Y")
# ajoute X, Y dans la collection 'vars', il sera appelé ultérieurement
tf.add_to_collection('vars', X)
tf.add_to_collection('vars', Y)
# weights est une matrice, le nb de ligne = feature_size et le nb de colonne est le nb de labels
#la variable w sera générée aléatoirement selon une distribution normale, 
weights = tf.Variable(tf.random_normal([feature_size,label_size],
                                       # 正态分布平均数
                                       mean=0,
                                       # 方差
                                       stddev=(np.sqrt(6/feature_size+
                                                         label_size+1)),
                                       name="weights"))
# matrice biais sera générée aléatoirement selon distribution normale, le nb de ligne = 1, nb de colonne = 3
bias = tf.Variable(tf.random_normal([1,label_size],
                                    mean=0,
                                    stddev=(np.sqrt(6/feature_size+label_size+1)),
                                    name="bias"))
# ajouter la matrice weights et bias dans la collection 'vars'
tf.add_to_collection('vars', weights)
tf.add_to_collection('vars', bias)

# initialisation des variables
init_OP = tf.global_variables_initializer()
apply_weights_OP = tf.matmul(X, weights, name="apply_weights")
# add_bias_OP = X*weight + biais 
add_bias_OP = tf.add(apply_weights_OP, bias, name="add_bias")
# fonction d'activiation
activation_OP = tf.nn.softmax(add_bias_OP, name="activation")
# lossfunction -> moindre carre 
cost_OP = tf.nn.l2_loss(activation_OP-Y, name="squared_error_cost")
# algorithme du gradient
training_OP = tf.train.GradientDescentOptimizer(learningRate).minimize(cost_OP)

# In[15]:

epoch_values=[]
accuracy_values=[]
cost_values=[]

# In[ ]:

# collection des données
sess = tf.Session()
sess.run(init_OP)
correct_predictions_OP = tf.equal(tf.argmax(activation_OP,1),tf.argmax(Y,1))
# taux d'exactitude
accuracy_OP = tf.reduce_mean(name="accuracy_OP",input_tensor=tf.cast(correct_predictions_OP, "float"))
activation_summary_OP = tf.summary.histogram("output", activation_OP)
accuracy_summary_OP = tf.summary.scalar("accuracy", accuracy_OP)
cost_summary_OP = tf.summary.scalar("cost", cost_OP)
weightSummary = tf.summary.histogram("weights", weights.eval(session=sess))
biasSummary = tf.summary.histogram("biases", bias.eval(session=sess))
all_summary_OPS = tf.summary.merge_all()
writer = tf.summary.FileWriter("summary_logs", sess.graph)
cost = 0
diff = 1

for i in range(numEpochs):
    if i > 1 and diff < .0001:
        print("change in cost %g; convergence."%diff)
        break
    else:
        # Run training step
        step = sess.run(training_OP, feed_dict={X: train_tags_feature, Y: train_Y})
        # Report occasional stats
        if i % 10 == 0:
            # Add epoch to epoch_values
            epoch_values.append(i)
            # Generate accuracy stats on test data
            summary_results, train_accuracy, newCost = sess.run(
                #'''accuracy_OP-1'''
                [all_summary_OPS, accuracy_OP, cost_OP],
                feed_dict={X: train_tags_feature, Y: train_Y}
            )
            # Add accuracy to live graphing variable
            accuracy_values.append(train_accuracy)
            # Add cost to live graphing variable
            cost_values.append(newCost)
            # Write summary stats to writer
            writer.add_summary(summary_results, i)
            # Re-assign values for variables
            diff = abs(newCost - cost)
            cost = newCost

            #generate print statements
            print("step %d, training accuracy %g"%(i, train_accuracy))
            print("step %d, cost %g"%(i, newCost))
            print("step %d, change in cost %g"%(i, diff))

            time.sleep(1)

print("final accuracy on test set: %s" %str(sess.run(accuracy_OP, feed_dict={X: train_tags_feature, Y: train_Y})))


# enregisitrer le model, la session d'entrainement
saver = tf.train.Saver() 
saver.save(sess, args.model+"/" + "model.ckpt")  
sess.run(bias)



