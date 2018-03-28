#!/bin/python3
#coding : utf8

import sys
from lxml import etree
import gensim


class PreparationCorpus():

    def __init__(self, fichier):

        try:
            f = open(fichier, 'r', encoding="utf-8")
        except IOError:
            print("Impossible d'ouvrir {}".format(fichier))
            sys.exit(2)
        else:
            with f:
                tree = etree.parse(f)

                self.documents_type = [doc.get("class") for doc in tree.xpath("//doc")]
                self.documents = list()

                for doc in tree.xpath("//treetagger"):
                    doc = doc.text
                    tmp = []
                    for token in doc.split(' '):
                        token_split = token.split('/')
                        lemme = token_split[2]
                        if token_split[2] == "<unknown>":
                            lemme = token_split[0].lower()
                        tmp.append(lemme)

                    (self.documents).append(tmp)

    def getDocumentsType(self):
        return self.documents_type

    def getDocuments(self):
        return self.documents


def main():

    # Modifier le chemin si nécessaire
    corpus = PreparationCorpus("../Corpus/all-train.xml")

    #print(corp.getDocumentsType())
    documents = corpus.getDocuments()


    # Word2Vec
    model = gensim.models.Word2Vec(documents, size=100, window=5, min_count=2, workers=4)
    #print(model.wv.vocab)
    #print(model.wv["akhenaton"])

    # TF IDF
    dictionary = gensim.corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(document) for document in documents]
    tf_idf = gensim.models.TfidfModel(corpus)
    #print(tf_idf[corpus[0]])

    # Ajouter TensorFlow

if __name__ == "__main__":
    main()
