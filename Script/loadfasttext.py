#!/bin/env python3

import fasttext

model = fasttext.load_model("frtenten12_1.bin")

print(model['arbre'])
print(model['sapin'])

from scipy.spatial.distance import cosine
print(cosine(model['arbre'], model['sapin']))
print(cosine(model['chêne'], model['sapin']))
print(cosine(model['handball'], model['football']))
print(cosine(model['handball'], model['sapin']))


