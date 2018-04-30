#!/bin/env python3
'''
	Auteurs : FAVIA Giovanna - HELMAN Agathe - SCARCELLA Nicolas
	Date : AVRIL 2018
	
	Ce programme prétraite le corpus italien italien_corpus.xml en produisant en sortie un fichier XML ayant, por chaque article: une balise contenant le texte, une autre sa version lemmatisée et taggée et une dernière avec sa version sous-forme de bigrams.
	
	Lancement: python3 Corpus2Treetagger.py
	
'''
from treetagger import TreeTagger
import re

import nltk
from nltk import word_tokenize
from nltk.util import ngrams

def litTexteDuFichierUtf8 (fichier):
	fh = open(fichier, 'r', encoding="utf-8") 
	texteFichier = fh.read() 
	fh.close() 
	return texteFichier

def lemmatisation (texte):
	tt_it=TreeTagger(language="italian")
	texte = tt_it.tag(texte)
	liste_lemme=[]
	for liste in texte:
		if liste[2] == "<unknown>" or liste[2] == "@card@":
			liste_lemme.append(liste[0])
			liste_lemme.append(liste[1] + "/")
		else:
			liste_lemme.append(liste[2])
			liste_lemme.append(liste[1] + "/")
	string = ' '.join(liste_lemme)
	return(string)
	
def get_lemme (texte):
	tt_it=TreeTagger(language="italian")
	texte = tt_it.tag(texte)
	liste_lemme=[]
	for liste in texte:
		if liste[2] != "<unknown>" or liste[2] == "@card@":
			liste_lemme.append(liste[2])
		else:
			liste_lemme.append(liste[0])
		string = ' '.join(liste_lemme)
	return(string)

def metTexteEnMinuscule (texte):
	texte = texte.lower()
	return texte

def enleveAccentsDuTexte (texte):
	texte = re.sub ('[ò]', 'o', texte)
	texte = re.sub ('[ì]', 'i', texte)
	texte = re.sub ('[à]', 'a', texte)
	texte = re.sub ('[ù]', 'u', texte)
	texte = re.sub ('[è]', 'e', texte)
	texte = re.sub ('[é]', 'e', texte)
	# texte = re.sub ('[,]', '', texte)
	# texte = re.sub ('[.]', '', texte)
	return texte

def make_bigrams (texte):
	token = nltk.word_tokenize(texte)
	bigrams = ngrams(token,2)
	return bigrams

'''************************'''
from lxml import etree

tree = etree.parse('italien_corpus.xml')
root = tree.getroot()
doc = root.xpath('/corpus/doc')
texte = root.xpath('/corpus/doc/descendant::*')

D = open ('italien_corpus_Treetagger.xml', 'w+')
D.write("<?xml version=\"1.0\" encoding='UTF-8'?>\n")
D.write("<corpus>\n")

for doc in root:
	classe = doc.attrib.get('class')
	titre = doc.attrib.get('title')
	source = doc.attrib.get('source')
	D.write("<doc class=\""+classe+"\" "+"title=\""+titre+"\" "+"source=\" "+source+"\">")
	D.write("\n<text>")
	for texte in doc:
		texte = texte.text
		D.write(texte)
		D.write("</text>\n")
		D.write("<treetagger_title>")
		treetagger_title = (enleveAccentsDuTexte(lemmatisation(titre)))
		D.write (treetagger_title)
		D.write("</treetagger_title>")
		D.write("<treetagger>\n")
		treetagger_texte = (enleveAccentsDuTexte(lemmatisation(texte)))
		D.write(treetagger_texte)
		D.write("\n</treetagger>\n")
		# treetagger_pos = get_POS(texte)
		# D.write(treetagger_pos)
		D.write("<bigrams>")
		bigrams = (make_bigrams(metTexteEnMinuscule(get_lemme(texte))))#it's a generator
		bigrams=list(bigrams) #it's a list
		bigrams=' '.join(map(str, bigrams))#it's a tuple
		bigrams = ''.join(bigrams) #it' a string
		bigrams = bigrams.replace("\'", "")
		bigrams = bigrams.replace(",", "")
		bigrams = enleveAccentsDuTexte(bigrams)
		D.write(bigrams)
		D.write("</bigrams>")
		D.write("</doc>\n")
D.write("</corpus>")




