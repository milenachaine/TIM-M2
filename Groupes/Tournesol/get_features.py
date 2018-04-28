#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Jielei Li - Mingqiang Wang - Arthur Provenier

    Permet de savoir si la feature est présente dans le texte
    pour construire la matrice
"""


def getfeature(texte, feature_name):

    # Si la feature est dans le texte, renvoi 1
    # sinon 0
    if feature_name in texte:
        return 1
    return 0
