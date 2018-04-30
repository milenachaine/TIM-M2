
# coding: utf-8

# In[1]:

import xml.etree.ElementTree as ET
import string 
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from treetagger import TreeTagger
import re
import pickle
import numpy as np
import pandas as pd
from normalize_functions import *


# In[2]:

#récuperer le texte
fic='../data/test.xml'
f=open(fic,'r')
tree = ET.parse(f)
root = tree.getroot()
data=[]

stopwords_file="../data/stopwords_fr.txt"
stopwords=open(stopwords_file,'r').read().splitlines()

newtext=[]

#w=open('../data/test.csv', 'w') 
for doc in root :
    if doc.get('class') == 'fake':
        texte=doc.text
        
        ### normalize functions ###
        texte=removenumbers(texte)
        texte=lowercase(texte)
        texte=removeponctuation(texte)
        texte=Removeaddspaces(texte)
        texte=tokenize(texte)
        texte=removestopword(texte)
        texte=lemmatise(texte)
        #################
        
        texte = "fake"+"\t"+ texte+"\n"
        
        #create a csv file
        #w.write(texte)
        
        data.append(texte)
    
    if doc.get('class') == 'trusted':
        texte=doc.text
        
        ### normalize functions ###
        texte=removenumbers(texte)
        texte=lowercase(texte)
        texte=removeponctuation(texte)
        texte=Removeaddspaces(texte)
        texte=tokenize(texte)
        texte=removestopword(texte)
        texte=lemmatise(texte)
        #################
        
        texte="trusted"+"\t"+texte+"\n"
        
        #create a csv file
        #w.write(texte)
        
        data.append(texte)
    
    if doc.get('class') == 'parodic':
        texte=doc.text
        ### normalize functions ###
        texte=removenumbers(texte)
        texte=lowercase(texte)
        texte=removeponctuation(texte)
        texte=Removeaddspaces(texte)
        texte=tokenize(texte)
        texte=removestopword(texte)
        texte=lemmatise(texte)
        #################
        
        texte="parodic"+"\t"+texte+"\n"
        
        #create a csv file
        #w.write(texte)
        
        data.append(texte)   
        


# In[3]:

# split sur chaque texte
data_split = [x.split('\t') for x in data if len(x)>=1]

print(data_split)
# In[4]:

#save data_split variable with pickl
path = "../tests/tests.data"
with open(path, 'wb') as fi: 
    pickle.dump(data_split, fi, protocol=pickle.HIGHEST_PROTOCOL)






