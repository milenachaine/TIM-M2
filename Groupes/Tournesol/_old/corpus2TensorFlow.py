#!/bin/python3
#coding : utf8

import sys
from lxml import etree
import gensim

def read_corpus(fichier):
    """Lecture du fichier et sauvegarde de la classe du documents
    ainsi que son contenu textuel"""

    print('Reading corpus')
    try:
        with open(fichier, 'r') as f:
            tree = etree.parse(f)

            docs_class = [doc.get("class") for doc in tree.xpath("//doc")]
            docs_text = [doc.text for doc in tree.xpath("//treetagger")]
    except IOError:
        print("Erreur d'ouverture de : {}".format(fichier))
        sys.exit(2)
    return docs_class, docs_text

def token_to_lemme(lst_docs):
    """Prend une liste de listes et retourne
    une nouvelle liste de listes contenant les lemmes"""

    docs = list() # Liste de listes (docs) contenant des str
    for doc in lst_docs:
        tmp = []
        for token in doc.split(' '):
            token_split = token.split('/')
            lemme = token_split[2]
            if token_split[2] == "<unknown>":
                lemme = token_split[0].lower()
            tmp.append(lemme)

        docs.append(tmp)
    return docs

def main():

    # Modifier le chemin si nécessaire
    document_type, document_raw = read_corpus("../Corpus/all-train.xml")
    documents = token_to_lemme(document_raw)


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
