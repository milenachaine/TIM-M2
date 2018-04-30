
# coding: utf-8

# In[1]:

import xml.etree.ElementTree as ET
import string 
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from treetagger import TreeTagger
import re
import pickle


# In[2]:

# functions

def removestopword(text):
    newtext=[]
    stopwords_file="../data/stopwords_fr.txt"
    stopwords=open(stopwords_file,'r').read().splitlines()
    for word in text.split():
        if word not in stopwords:
            newtext.append(word)
    text=' '.join(newtext)
    return str(text)


# In[3]:

def tokenize(text):
    toks=nltk.word_tokenize(text)
    text= ' '.join(toks)
    return str(text)


# In[4]:

def lowercase(text):
    return text.lower()


# In[5]:

def removeponctuation(text):
    text=''.join(c for c in text if c not in string.punctuation)
    return text


# In[6]:

def removenumbers (text):
    text=''.join(c for c in text if c not in '0123456789')
    return str(text)


# In[7]:

def Removeaddspaces (text):
    return ' '.join(text.split())


# In[8]:

def lemmatise(text):
    pat=re.compile("(.+)|(.+)")
    listtext=[]
    tt = TreeTagger(language='french')
    texte=tt.tag(text)
    for tags in texte:
        mot=tags[2]
        if mot=="<unknown>":
            mot=tags[0]
            listtext.append(mot)
        else:
            match = re.search("(.+)\\|.+", mot)
            if match:
                mot = match.group(1) 
                listtext.append(mot)
            else:
                listtext.append(mot)
        text= ' '.join(listtext)
        lemmetext=str(listtext)
    return text    


# In[9]:
##### golobal function

def normalize(text):
    text=removenumbers(text)
    text=lowercase(text)
    text=removeponctuation(text)
    text=Removeaddspaces(text)
    text=tokenize(text)
    text=removestopword(text)
    text=lemmatise(text)
    return text

