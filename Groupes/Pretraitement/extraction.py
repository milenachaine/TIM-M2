import os  
import sys 
import re
from collections import Counter
pasmot=re.compile("\W+")
seg=re.compile("(\s*\/\s*|\()")
elim=re.compile("\s*\([^)]*\)\s*")
total=open("D:\\Cours\\Apprentissage\\TIM-M2\\Groupes\\Prétraitement\\phrases.txt", "r", encoding="utf-8").read().lower()
words=Counter(pasmot.split(total))
terme=re.sub(seg, "\n", re.sub(elim,'\n',open("D:\\Cours\\Apprentissage\\TIM-M2\\Groupes\\Prétraitement\\termes_juridiques.txt", "r", encoding="utf-8").read())).replace(")", "" ).split("\n")

juri_term=set()
for i in terme:
    juri_term.add(i.replace("\xa0", " ").strip())
	
#dico=dict()
with open("jury_words.txt", "w", encoding="utf-8") as j:
    for expression in juri_term:
        if " " in expression:
            if total.count(expression.lower())>0:
                j.write(expression+"\t"+str(total.count(expression.lower()))+"\n")
            #dico[expression.lower()]=total.count(expression.lower())
        else:
            if expression and expression.lower() in words:
                j.write(expression+"\t"+str(words[expression.lower()])+"\n")
            #dico[expression.lower()]=words[expression.lower()]
        