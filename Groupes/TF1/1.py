import pprint
import treetaggerwrapper
file=open('/Users/Valerian/Desktop/TIM-M2/Corpus/all.xml', 'r')
texte=[]
for line in file:
    texte.append(line)
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr')
    tags = tagger.tag_text(texte)
    print(tags)