from treetaggerwrapper import TreeTagger, make_tags
TAGGER = TreeTagger(TAGLANG='fr',TAGOPT="-token -lemma -sgml -no-unknown") 
import sys
import os
def main():
    phrase=sys.argv[1]
    line=""
    tags = TAGGER.tag_text(phrase)
    for tag in tags:
        line+=tag.replace("\t","/")+" "
    print("tagged phrase : "+line)
    return line
if __name__ == "__main__":
    main()
    
