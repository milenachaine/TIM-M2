
import sys
import os
import spacy
import xml.etree.ElementTree as ET
nlp = spacy.load('fr', vectors=False)
mydir=sys.argv[2]
phrases=open("phrases.txt", "w", encoding="utf-8")
if not os.path.exists(mydir):
    os.makedirs(mydir)
tree = ET.parse(sys.argv[1])
corpus = tree.getroot()
for i in corpus.findall("./doc"):
    cat = i.get('class')
    sub = i.get('subclass')
    ID = i.get('id')
    if not os.path.exists(mydir+"/"+cat+"/"+sub+"/"+ID):
        os.makedirs(mydir+"/"+cat+"/"+sub+"/"+ID)  
    for q in i.findall("./question"):
        ID_q=q.get("number")
        with open(mydir+"/"+cat+"/"+sub+"/"+ID+"/"+ID+"_q"+ID_q+".conllu", "w", encoding="utf-8") as question:
            doc = nlp(q.text.strip())
            for sent in doc.sents:
                question.write("#"+sent.text.strip()+'\n')
                for index, word in enumerate(sent):
                    if word.head == word:
                        head_idx = 0
                    else:
                        head_idx = doc[index].head.i+1
                    question.write(str(index+1)+"\t"+word.text+"\t"+word.lemma_+"\t"+word.pos_+"\t"+'_'+"\t"+word.tag_+"\t"+str(head_idx)+"\t"+word.dep_+"\t"+'_'+"\t"+'_'+"\n")
                question.write("\n\n")
                phrases.write(sent.text.strip()+"\n")
    for a in i.findall("./answer"):
        ID_a=a.get("number")
        with open(mydir+"/"+cat+"/"+sub+"/"+ID+"/"+ID+"_a"+ID_a+".conllu", "w", encoding="utf-8") as answer:
            doc = nlp(a.text.strip())
            for sent in doc.sents:
                answer.write("#"+sent.text.strip()+'\n')
                for index, word in enumerate(sent):
                    if word.head == word:
                        head_idx = 0
                    else:
                        head_idx = doc[index].head.i+1
                    answer.write(str(index+1)+"\t"+word.text+"\t"+word.lemma_+"\t"+word.pos_+"\t"+'_'+"\t"+word.tag_+"\t"+str(head_idx)+"\t"+word.dep_+"\t"+'_'+"\t"+'_'+"\n")
                answer.write("\n\n")
                phrases.write(sent.text.strip()+"\n")
phrases.close()

    
 
