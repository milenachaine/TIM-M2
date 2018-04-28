#!/bin/bash

echo "Build and split corpus"
# python3 buildcorpus.py
python3 corpussplit.py ../Corpus/all.xml

for g in lstsq scikit-learn Tournesol; do
	echo "== TRAIN PREDICT $g =="
	python3 ../Groupes/$g/train.py ../Corpus/all-train.xml model
	python3 ../Groupes/$g/predict.py ../Corpus/all-test.xml model predictions.xml
	python3 xmlevaluate.py predictions.xml
	rm model predictions.xml
    
    # Pour le modele créé par Tensorflow ... 
    if [ "$g" == "Tournesol" ]; then
        rm model* checkpoint
    fi
done
