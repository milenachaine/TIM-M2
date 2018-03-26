#!/bin/env python3

import re
from gettfidf import gettfidf
features={}
for f in gettfidf('all.xml'):
    features[f]='numeric'

def getfeature(doc, name):

    text = doc.find('text').text
    tt = doc.find('treetagger').text
    tokenlst = [tok.split('/') for tok in tt.split(' ')]
    for feature in features :
        if name == feature:
            nbpresse = 0
            nbpresse += text.count('presse')
            nbpresse += text.count('presses')
            return nbpresse