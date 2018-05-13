#!/bin/env python3
# -*- coding: utf8 -*-

import re

def russia_count(text, pos, lemmas):
    return lemmas.count("Russie")

def i_count(text, pos, lemmas):
    return lemmas.count("je")

def punct_count(text, pos, lemmas):
    return pos.count("PUN:cit")

def adv_count(text, pos, lemmas):
    return pos.count("ADV")


# def china_count(text, pos, lemmas):
#     return lemmas.count("Chine")

# def usa_count(text, pos, lemmas):
#     return len(re.findall(r"\bUSA?\b", text))

# def you_count(text, pos, lemmas):
#     return lemmas.count("vous")

# def united_states_count(text, pos, lemmas):
#     return len(re.findall(r"\b[EÉ]tats-Unis\b", text))