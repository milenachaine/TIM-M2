
# coding: utf-8

# In[62]:


#!/bin/env python3

import xml.etree.ElementTree as ET

file = open("all_lexico_appr.txt", "w", encoding="UTF-8")
alldocs = ET.Element('corpus')
i = 0

for etudiant in open('../../Corpus/etudiants.lst').readlines():
	xmlfile = '../../Corpus/Etudiants/' + etudiant.strip() + '.xml'
	#print('Processing', xmlfile)
	xmlcorpus = ET.parse(xmlfile)
    
	for doc in xmlcorpus.findall('doc'):
		partie = doc.get('class')
		i += 1        
		if partie == "fake":
			partie1 = doc.text   
			fake = "{}{}{}{}".format("<fake=", i, ">", partie1)
			file.write(fake)
		elif partie == "trusted":
			partie2 = doc.text
			trusted = "{}{}{}{}".format("<trusted=", i, ">", partie2)
			file.write(trusted)
		else:
			partie3 = doc.text
			parodic = "{}{}{}{}".format("<parodic=", i, ">", partie3)
			file.write(parodic)