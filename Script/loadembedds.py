#!/bin/env python3

from gensim import models

models.KeyedVectors.load_word2vec_format('frtenten12_1.vec', binary=False)



