#!/bin/env python3

text = "Au lendemain d’embouteillages monstres autour de Paris, de nouvelles chutes de neige sont attendues dans la matinée en Ile-de-France mais également sur la moitié nord du pays. Mardi à 23 heures, Météo France a relevé 6 centimètres à Tours, 7 cm à Paris-Montsouris, 9 cm à Blois, 11 cm à Orléans, 13 cm à Chartres. L’institut attend dans la matinée de mercredi entre 7 et 15 cm sur les départements placés en vigilance orange et jusqu’à 20 cm localement."

text = "Ils président le conseil"

print(text)

print('PREPROC NLTK')
import nltk
sents = nltk.sent_tokenize(text, language = 'french')
for sent in sents:
	tokenized = nltk.word_tokenize(text, language = 'french')
	tagged = nltk.pos_tag(tokenized)
	print(tagged)
 
print('PREPROC Spacy')
import spacy
nlp = spacy.load('fr')
doc = nlp(text)
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

print('PREPROC TreeTagger')
import pprint
import treetaggerwrapper
tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr')
tags = tagger.tag_text(text)
pprint.pprint(tags)
