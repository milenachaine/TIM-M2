import requests
from bs4 import BeautifulSoup
import string
import spacy 
a="https://www.dictionnaire-juridique.com/"
req2 = requests.get(a)
soup2 = BeautifulSoup(req2.text, "lxml")

termes_juridique=[]
non=[i for i in string.ascii_lowercase]
for i in soup2.find_all("a"):
    if i.text.lower() not in non:
        termes_juridique.append(i.text)

del termes_juridique[:7]
for i in termes_juridique : 
    if i == "":
        termes_juridique.remove(i)

with open("termes_juridiques.txt","w",encoding="utf-8") as fic:
    for i in termes_juridique : 
        fic.write(i)
        fic.write("\n")

nlp = spacy.load('fr_core_news_sm', vectors=False)
termes_annotees=[]
for i in termes_juridique:
    doc=nlp(i)
    for i in doc:
        termes_annotees.append((i.text,i.pos_))
		
with open("termes_juridiques_annotés.txt","w",encoding="utf-8") as fic:
    for i in termes_annotees : 
        fic.write(i[0]+"\t"+i[1])
        fic.write("\n")