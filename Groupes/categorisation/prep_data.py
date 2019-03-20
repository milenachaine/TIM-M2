"""Serialisation du corpus.


    USAGE : python3 prep_data.py <PATH_TO_XML_SRC> <PATH_TO_PICKLE_DST>
"""
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys
import pickle
from settings import DOC_CLASS
from corpus import *

def main():
    tree = ET.ElementTree(file=sys.argv[1])
    corpus = list()
    for doc in tree.getroot():
        question = " ".join([q.text.strip() for q in doc.findall(
            "question")]).strip()
        if not question:
            continue
        qa = JurQA()
        qa.class_ = DOC_CLASS[doc.get("class").lower()]
        qa.question.init_text(question)
        corpus.append(qa)

    pickle.dump(corpus,file=open(sys.argv[2], 'wb'))

if __name__ == "__main__":
    main()