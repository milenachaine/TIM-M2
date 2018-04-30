#!/bin/env python3
# -*- coding: utf-8 -*-
# author : Yuran ZHAO & Audrey CORNU INALCO M2 TAL IM
# usage: python3 train.py

import xml.etree.ElementTree as ET
import os.path, argparse
import re
import sys
from imp import reload 
reload(sys)
import numpy as np
import keras
from keras.layers import Dense, Input, Flatten, Dropout
from keras.layers import Conv1D, MaxPooling1D, Embedding, GlobalMaxPooling1D
from keras.models import Sequential
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical


'''
pretraitrement du corpus:
xml à txt
1) txt qui contient le contenu
2) txt qui contient label de catégorie (fake, trusted et parodic)
'''
def pretraitement(xml):
  print("Lire input corpus")
  tree = ET.parse(xml)
  root = tree.getroot()
  print('creer les fichiers de corpus')  
  for doc in root.findall('doc'):
    label = doc.get('class')
    print(label)
    if label == "fake":
      label = "1"
    if label == "trusted":
      label = "2"
    else:
      label = "3"
    txt = doc.find('text').text
    txt = txt.replace("\n","")
    txt = re.split(' ',txt)
  #  ecrit(txt, label)
  print("xml ---> txt")

'''
ecrire les données dans les fichiers txt
'''
def ecrit(txt, label):
  from getfeatures import features
  with (open("train.txt",'a', encoding="utf-8")) as train:
    with(open("train_label.txt",'a', encoding="utf-8")) as train_label:
      with (open("test.txt",'a', encoding="utf-8")) as test:
        with(open("test_label.txt",'a', encoding="utf-8")) as test_label:
          i = 0
          for t in txt:
            # get features
            for f in features:
              if t == f:
                if i % 2 == 0:
                  train.write(t)
                  train.write("\n")
                  train_label.write(label+"\n")
                  i = i + 1
                else:
                  test.write(t)
                  test.write("\n")
                  test_label.write(label+"\n")
                  i = i + 1
'''
training 
creer le modele 
'''
def train(train_txt, train_label):
  print(" +++++++++++++++++ train +++++++++++++++++")
  MAX_SEQUENCE_LENGTH = 100
  EMBEDDING_DIM = 200
  VALIDATION_SPLIT = 0.36

  print("++++++++++++ charger le corpus +++++++++++ ")
  train_texts = open(train_txt).read().split('\n')
  train_labels = open(train_label).read().split('\n')

  all_labels = []
  for a in train_labels:
    if len(a) != 0:
      all_labels.append(int(a))

  print ('+++++++++ text à var ++++++++++++ ')
  tokenizer = Tokenizer()
  tokenizer.fit_on_texts(train_texts)
  sequences = tokenizer.texts_to_sequences(train_texts)
  word_index = tokenizer.word_index
  print('Found %s unique tokens.' % len(word_index))
  data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
  print('Shape of data tensor:', data.shape)
  labels = to_categorical(np.asarray(all_labels))
  print('Shape of label tensor:', labels.shape)

  print ("++++++++++ separer data +++++++++")
  # separer le data en deux parties: train et validation
  p1 = int(len(data)*(1-VALIDATION_SPLIT))
  x_train = data[:p1]
  y_train = labels[:p1]
  x_val = data[p1:]
  y_val = labels[p1:]
  print ('text pour train: '+str(len(x_train)))
  print ('text pour validation: '+str(len(x_val)))
  print ('++++++++++++++++ training model +++++++++++++++++')
  # construction de reseau avec une couche en modele CNN
  model = Sequential()
  model.add(Embedding(len(word_index) + 1, EMBEDDING_DIM, input_length=MAX_SEQUENCE_LENGTH))
  model.add(Dropout(0.2))
  # convolution and rectified linear activation.
  model.add(Conv1D(250, 3, padding='valid', activation='relu', strides=1))
  # max pooling
  model.add(MaxPooling1D(3))
  model.add(Flatten())
  model.add(Dense(EMBEDDING_DIM, activation='relu'))
  model.add(Dense(labels.shape[1], activation='softmax'))
  model.summary()
  model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['acc'])
  print(model.metrics_names)
  model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=2, batch_size=128)
  model.save('cnn.h5')

if __name__ == "__main__":
  #pretraitement("all.xml")
  train("train.txt", "train_label.txt")


