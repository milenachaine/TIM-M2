# requirements : treetaggerwrapper

from treetaggerwrapper import TreeTagger, make_tags
if 'teampath' in locals() or 'teampath' in globals():
    TAGGER = TreeTagger(TAGLANG='fr',TAGOPT="-token -lemma -sgml -no-unknown", TAGDIR="/home/teamlaw/TreeTagger/")
else:
    TAGGER = TreeTagger(TAGLANG='fr',TAGOPT="-token -lemma -sgml -no-unknown")

class JurQA:
    def __init__(self):
        self.class_ = str()
        self.subclass_ = str()
        self.question = Text()
        self.answer = Text()

class Text:
    def __init__(self):
        self.text = list()
        self.lemma = list()
        self.pos = list()


    def init_text(
            self,
            text
    ):
        tags = TAGGER.tag_text(text)
        for tag in tags:
            try:
                word, pos, lemma = tag.split("\t")
            except:
                continue
            self.text.append(word)
            self.lemma.append(lemma)
            self.pos.append(pos)

    def tagged_text(self):
        return list(zip(self.text,self.lemma,self.pos))

