#!/bin/bash

echo "Retrieve corpora"
cd Crawling
scp -oUser=teamlaw -P 2251 helium.lab.parisdescartes.fr:~/Corpus/CorpusJuritravailVersion1.xml CorpusJuritravailVersion1.xml
scp -oUser=teamlaw -P 2251 helium.lab.parisdescartes.fr:~/Corpus/corpusIrisVersion4.xml corpusIrisVersion4.xml

echo "Prepare data and learn classifier"
cd ../categorisation/
python3 prep_data.py ../Crawling/corpusIrisVersion4.xml ../Crawling/corpusIrisVersion4.pkl
python3 classifier.py -c rf -f lemma+pos -o modelIrisLP.mdl ../Crawling/corpusIrisVersion4.pkl

echo "Preprocess data for similarities"
cd ../Similarite/
python3 preprocessdocs.py
