import polyglot
from collections import Counter
from polyglot.downloader import downloader
downloader.download("embeddings2.fr")
downloader.download("ner2.fr")
from polyglot.text import Text
ents=[]
taille=len(open("phrases.txt", "r", encoding="utf-8").readlines())
print(taille)
with open("phrases.txt", "r", encoding="utf-8") as p:
    for i in range(taille):
        print(i)
        texte=Text(p.readline().strip())
        try:
            for entity in texte.entities:
                        #ents.append(" ".join(entity))
                #print(entity)
                ents.append(" ".join(entity))
        except:
            pass
        continue
dico=Counter(ents)
#print(dico)
with open("ents.txt", "w", encoding="utf-8") as e:
    new=sorted(dico.items(), key=lambda t:t[1], reverse=True)
    for k,v in new:
        #print(k, dico[k])
        e.write(str(k)+"\t"+str(v)+"\n")
    
 
