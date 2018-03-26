#!/bin/bash

python3 buildcorpus.py
python3 corpussplit.py ../Corpus/all.xml
python3 ../Groupes/lstsq/train.py ../Corpus/all-train.xml model
python3 ../Groupes/lstsq/predict.py ../Corpus/all-test.xml model predictions.xml
python3 xmlevaluate.py predictions.xml
rm model predictions.xml
