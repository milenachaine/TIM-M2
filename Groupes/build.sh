#!/bin/bash

echo "Retrieve corpora"
cd Crawling
[[ -f CorpusJuritravailVersion1.xml ]] || scp  -P 2251 teamlaw@helium.lab.parisdescartes.fr:~/Corpus/CorpusJuritravailVersion1.xml .
[[ -f corpusIrisVersion4.xml ]] || scp -P 2251 teamlaw@helium.lab.parisdescartes.fr:~/Corpus/corpusIrisVersion4.xml .

echo "Retrieve preprocessed files"
cd ../Pretraitement/
[[ -d juritravail ]] || scp -r -P 2251 teamlaw@helium.lab.parisdescartes.fr:/home/chuanming/pretraitement/juritravail .
[[ -d net-iris ]] || scp -r -P 2251 teamlaw@helium.lab.parisdescartes.fr:/home/chuanming/pretraitement/net-iris .

echo "Prepare data and learn classifier"
cd ../categorisation/
python3 prep_data.py ../Crawling/corpusIrisVersion4.xml ../Crawling/corpusIrisVersion4.pkl
python3 classifier.py -c rf -f lemma+pos -o modelIrisLP.mdl ../Crawling/corpusIrisVersion4.pkl

echo "Preprocess data for similarities"
cd ../Similarite/
python3 preprocessdocs.py
