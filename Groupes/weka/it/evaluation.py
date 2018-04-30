from lxml import etree
import sys

if len(sys.argv) == 2:
	path = sys.argv[1]
else:
	print("Rentrer le fichier résultat de la prédiction")
	sys.exit(1)

tree = etree.parse(path)
root = tree.getroot()
doc = root.xpath('/corpus/doc')
texte = root.xpath('/corpus/doc/descendant::*')

'''RAPPEL'''
#nb docs correctement attribué à la classe i / nb docs appartenants à la classe i
cpt_trusted = 0
cpt_predict_trusted=0
for doc in root:
	classe = doc.attrib.get('class')
	classe_predict = doc.attrib.get('classpredict')
####classe trusted####
	if classe == "trusted":
		cpt_trusted+=1
		# print("classe trusted : ", cpt_trusted)
		if classe == classe_predict:
			cpt_predict_trusted+=1
			# print("classe predicted trusted : ", cpt_predict_trusted)
rappel_trusted = cpt_predict_trusted/cpt_trusted
print("RAPPEL pour la classe TRUSTED : ", rappel_trusted)

####classe fake####
cpt_fake = 0
cpt_predict_fake=0
for doc in root:
	classe = doc.attrib.get('class')
	classe_predict = doc.attrib.get('classpredict')
####classe fake####
	if classe == "fake":
		cpt_fake+=1
		# print("classe fake : ", cpt_fake)
		if classe == classe_predict:
			cpt_predict_fake+=1
			# print("classe predicted fake : ", cpt_predict_fake)
rappel_fake = cpt_predict_fake/cpt_fake
print("RAPPEL pour la classe FAKE : ", rappel_fake)


####classe parodic####
cpt_parodic = 0
cpt_predict_parodic=0
for doc in root:
	classe = doc.attrib.get('class')
	classe_predict = doc.attrib.get('classpredict')
####classe fake####
	if classe == "parodic":
		cpt_parodic+=1
		# print("classe parodic : ", cpt_parodic)
		if classe == classe_predict:
			cpt_predict_parodic+=1
			# print("classe predicted parodic : ", cpt_predict_parodic)
rappel_parodic = cpt_predict_parodic/cpt_parodic
print("RAPPEL pour la classe PARODIC : ", rappel_parodic)

###############RAPPEL des 3 classes##################

somme_rappel = rappel_trusted+rappel_fake+rappel_parodic
rappel = somme_rappel/3

print("Le rappel global est de : ", rappel)

'''PRECISION'''
#nb docs correctement attribués à la classe i / nb docs attribués à la classe i

cpt_trusted = 0
cpt_predict_trusted=0
for doc in root:
	classe = doc.attrib.get('class')
	classe_predict = doc.attrib.get('classpredict')
####classe trusted####
	if classe_predict == "trusted":
		cpt_predict_trusted+=1 #docs attribés à la classe
		# print("classe predicted trusted :", cpt_predict_trusted)
		if classe_predict == classe:
			cpt_trusted+=1 #docs correctement attribués
			# print("classe CORRECT predicted trusted : ", cpt_trusted)
precision_trusted = cpt_trusted/cpt_predict_trusted
print("PRECISION pour la classe TRUSTED : ", precision_trusted)

cpt_fake = 0
cpt_predict_fake=0
for doc in root:
	classe = doc.attrib.get('class')
	classe_predict = doc.attrib.get('classpredict')
####classe fake####
	if classe_predict == "fake":
		cpt_predict_fake+=1 #docs attribés à la classe
		# print("classe predicted fake :", cpt_predict_fake)
		if classe_predict == classe:
			cpt_fake+=1 #docs correctement attribués
			# print("classe CORRECT predicted fake : ", cpt_fake)
precision_fake = cpt_fake/cpt_predict_fake
print("PRECISION pour la classe FAKE : ", precision_fake)

cpt_parodic = 0
cpt_predict_parodic=0
for doc in root:
	classe = doc.attrib.get('class')
	classe_predict = doc.attrib.get('classpredict')
####classe fake####
	if classe_predict == "parodic":
		cpt_predict_parodic+=1 #docs attribés à la classe
		# print("classe predicted parodic :", cpt_predict_parodic)
		if classe_predict == classe:
			cpt_parodic+=1 #docs correctement attribués
			# print("classe CORRECT predicted parodic : ", cpt_parodic)
precision_parodic = cpt_parodic/cpt_predict_parodic
print("PRECISION pour la classe PARODIC : ", precision_parodic)

###############PRECISION des 3 classes##################

somme_precision = precision_trusted+precision_fake+precision_parodic
precision = somme_precision/3

print("La précision globale est de : ", precision)

'''F-Mesure'''
F = 2*(precision*rappel)/(precision+rappel)
print(path + " a une F-Mesure de: ",F)