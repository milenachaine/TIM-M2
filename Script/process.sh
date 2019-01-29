#!/bin/bash

python3 buildcorpus.py
python3 corpus2weka.py
python3 corpus2stats.py
python3 corpus2kmeans.py
