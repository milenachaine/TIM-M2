#!/bin/env python3
# -*- coding: utf-8 -*-
# author : Yuran ZHAO & Audrey CORNU INALCO M2 TAL IM

import xml.etree.ElementTree as ET
import os.path, argparse
import re
import numpy as np
import sys
from imp import reload 
import keras
from keras.layers import Dense, Input, Flatten, Dropout
from keras.layers import Conv1D, MaxPooling1D, Embedding, GlobalMaxPooling1D
from keras.models import Sequential
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.models import load_model

def predict(test_text, test_label,model):
  print("++++++++++++ charger le corpus +++++++++++ ")
  test_texts = open(test_text).read().split('\n')
  test_labels = open(test_label).read().split('\n')
  all_labels = []
  for a in test_labels:
    if len(a) != 0:
      all_labels.append(int(a))
  print ("+++++++++ text à var ++++++++++++ ")
  MAX_SEQUENCE_LENGTH = 100
  tokenizer = Tokenizer()
  tokenizer.fit_on_texts(test_texts)
  sequences = tokenizer.texts_to_sequences(test_texts)
  word_index = tokenizer.word_index
  print('Found %s unique tokens.' % len(word_index))
  data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
  print('Shape of data tensor:', data.shape)
  labels = to_categorical(np.asarray(all_labels))
  print('Shape of label tensor:', labels.shape)

  x_test = data[:]
  y_test = labels[:]
  print ('text pour tester: '+str(len(x_test)))

  model = load_model(model)
  print ('++++++++++++++++++ test model ++++++++++++++++++')
  print (model.evaluate(x_test, y_test))

if __name__ == "__main__":
  print("++++++++++++++++ avec features ++++++++++++++++++")
  predict("test.txt", "test_label.txt","cnn.h5")
  print("++++++++++++++++ sans features ++++++++++++++++++")
  predict("test_all.txt", "test_label_all.txt","cnn_all.h5")


