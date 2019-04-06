#!/usr/bin/python3
# -*- coding: utf-8 -*

# premier test parcours
import os

folder_path = "/Users/ferialyahiaoui/Documents/cours/S2/MACHINE_LEARNING/TIM-M2/Groupes/Pretraitement/Corpus"

for path, dirs, files in os.walk(folder_path):
    for filename in files:
        print(filename)
        print(os.path.abspath(filename))
