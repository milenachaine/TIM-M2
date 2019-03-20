from treetaggerwrapper import TreeTagger, make_tags
TAGGER = TreeTagger(TAGLANG='fr',TAGOPT="-token -lemma -sgml -no-unknown") 
import sys
import os
import xml.etree.ElementTree as ET
mydir=sys.argv[2]
phrases=open("phrases.txt", "w", encoding="utf-8")
if not os.path.exists(mydir):
    os.makedirs(mydir)
tree = ET.parse(sys.argv[1])
corpus = tree.getroot()
for i in corpus.findall("./doc"):
    source = i.get('source').strip().replace(" ","_")
    cat = i.get('class').strip().replace(" ","_")
    sub = i.get('subclass').strip().replace(" ","_")
    ID = i.get('id')
    if not os.path.exists(mydir+"/"+source+"/"+cat+"/"+sub+"/"+ID):
        os.makedirs(mydir+"/"+source+"/"+cat+"/"+sub+"/"+ID) 
    ID_q=1
    ID_a=1 
    for q in i.findall("./question"):
        with open(mydir+"/"+source+"/"+cat+"/"+sub+"/"+ID+"/"+ID+"_q"+str(ID_q)+".conll", "w", encoding="utf-8") as question:
            for line in q.text.split("\n"):
            #os.system('echo "'+line.strip().replace('"','\"')+'" | tree-tagger-french >>'+mydir+"/"+source+"/"+cat+"/"+sub+"/"+ID+"/"+ID+"_q"+str(ID_q)+".conll")
                tags = TAGGER.tag_text(line)
                for tag in tags:
                    question.write(tag+"\n")
                question.write("\n")
                
        #print(q.text.strip().replace('"','\"'))
        phrases.write(q.text.strip())
        ID_q+=1
    for a in i.findall("./answer"):
        with open(mydir+"/"+source+"/"+cat+"/"+sub+"/"+ID+"/"+ID+"_a"+str(ID_q)+".conll", "w", encoding="utf-8") as answer:
            for line in a.text.split("\n"):
            #os.system('echo "'+line.strip().replace('"','\"')+'" | tree-tagger-french >>'+mydir+"/"+source+"/"+cat+"/"+sub+"/"+ID+"/"+ID+"_q"+str(ID_q)+".conll")
                tags = TAGGER.tag_text(line)
                for tag in tags:
                    answer.write(tag+"\n")
                answer.write("\n")
        phrases.write(q.text.strip())
        ID_a+=1

#os.system("bash parcours.sh "+mydir+"/"+source)

phrases.close()

    
 
