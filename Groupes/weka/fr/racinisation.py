#!/bin/env python3
'''
	Auteurs : FAVIA Giovanna - HELMAN Agathe - SCARCELLA Nicolas
	Date : AVRIL 2018
	
	Ce programme traite le corpus (XML) d'articles en français en ajoutant une balise contenant, pour chaque article, les mots sous formes racinisés.
	
	Lancement: python3 racinisation.py
	
'''
from nltk.stem.snowball import SnowballStemmer
from lxml import etree
import re
import codecs

# Préparation du parsing
arbre = etree.parse("fr_corpus.xml")
racine = arbre.getroot()
d = racine.xpath("/corpus/doc")
stemmer = SnowballStemmer("french")

# OUverture d'un document XML de sortie
with codecs.open("fr_corpus_stem.xml", "w+", encoding="utf8") as f:
	f.write("<corpus>")
	for d in racine:
		# Attribution d'une variable à la valeur de chaque balise
		classe = d.attrib.get('class')
		titre = d.attrib.get('title')
		source = d.attrib.get('source')
		categorie = d.attrib.get('categorie')
		f.write("\n\t<doc class='"+classe+"' title='"+titre+"' source='"+source+"' categorie='"+categorie+"'>\n")
		
		t = d.text
		f.write('<texte>'+t+'</texte>\n')
		# Traitement et nettoyage du texte de chaque balise
		t = t.replace("\'", " ").replace("’", " ").replace(".", " ").replace(",", " ").replace("«", "« ").replace("»", " »").replace("(", "( ").replace(")", " )").replace("&", "&amp;")
		t = re.sub(".$", " ", t)
		t = t.split()
		f.write("<racinisation>\n")
		# Racinisation de chaque mot du texte
		for tok in t:
			radical = stemmer.stem(tok)
			f.write(radical+ " ")
		f.write("</racinisation>")
		f.write("</doc>")
	f.write("\n</corpus>")
	f.close()