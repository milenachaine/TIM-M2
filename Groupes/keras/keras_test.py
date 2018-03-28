#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 4 - Regressor example
import matplotlib
matplotlib.use('Agg')
import numpy as np
np.random.seed(1337)  # for reproducibility
import xml.etree.ElementTree as ET
import argparse
from getfeatures import features, getfeature
from keras.models import Sequential # 用来一层一层一层的去建立神经层
from keras.layers import Input # 意思是这个神经层是全连接层
from keras.layers import Dense # 意思是这个神经层是全连接层
import matplotlib.pyplot as plt # 可视化模块

aparser = argparse.ArgumentParser(description='Train model')
aparser.add_argument('input', help='Input file')
aparser.add_argument('model', help='Model file')
args = aparser.parse_args()

print('Reading corpus and finding features')
xmlcorpus = ET.parse(args.input)
nodoc = 0

# create some data
docs = xmlcorpus.getroot().getchildren()
featurekeys = sorted(list(features.keys()))
X = np.zeros((len(docs), len(featurekeys)))
Y = np.zeros((len(docs), 1))
#X = np.linspace(len(docs), len(featurekeys)+1, (130))

print('Insertion des données dans la matrice')
for i in range(len(docs)):
	for j in range(len(featurekeys)):
		doc = docs[i]
		featurename = featurekeys[j]
		X[i,j] = getfeature(doc, featurename)
		fake = 0
		if doc.get('class') == 'fake':
			fake = 1
		Y[i,0] = fake
X[:,-1] = 1

np.random.shuffle(X)    # randomize the data
#print("SIZE", x.shape)
# Y = 100 * X + 2 + np.random.normal(len(docs), 1, (130, ))

# plot data
# plt.scatter(X,Y)
# plt.show()

X_train, Y_train = X[:70], Y[:70]     # train 前 160 data points
X_test, Y_test = X[70:], Y[70:]       # test 后 40 data points

model = Sequential()
model.add(Dense(len(featurekeys), input_dim=len(featurekeys), kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))
# Compile model
model.compile(loss='mean_squared_error', optimizer='adam')

# model = Sequential() 
# model.add(Dense(units=1, input_dim=len(featurekeys))) # 在这个例子里只有一层
# model.compile(loss='mse', optimizer='sgd') # optimizer : 优化器

# train
print('Training -----------')
for step in range(100):
	cost = model.train_on_batch(X_train, Y_train)
	if step%10 == 0:
		print('train cost: ', cost)

# test
print('\nTesting ------------')
cost = model.evaluate(X_test, Y_test, batch_size=10)
print('test cost:', cost)
W, b = model.layers[0].get_weights()
print('Weights=', W, '\nbiases=', b)

#prediction
print(X_test)
Y_pred = model.predict(X_test)
print(Y_pred)
# plt.scatter(X_test, Y_test)
# plt.plot(X_test, Y_pred)
# plt.show()
