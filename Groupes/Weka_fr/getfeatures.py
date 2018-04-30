#!/bin/env python3
# -*- coding: utf8 -*-

import re

def russia_count(text, lemmas):
    # return 1 if "Russie" in lemmas else 0
    return lemmas.count("Russie")

def china_count(text, lemmas):
    # return 1 if "Chine" in lemmas else 0
    return lemmas.count("Chine")

def usa_count(text, lemmas):
    # return 1 if re.search(r"\bUSA?\b", text) is not None else 0
    return len(re.findall(r"\bUSA?\b", text))

def i_count(text, lemmas):
    # return 1 if "je" in lemmas else 0
    return lemmas.count("je")

def nice_count(text, lemmas):
    # return 1 if re.search(r"\bsympas?\b", text) is not None else 0
    return len(re.findall(r"\bsympas?\b", text))

def disease_count(text, lemmas):
    # return 1 if any(word in lemmas for word in ["tumeur", "cancer"]) else 0
    return sum(word in lemmas for word in ["tumeur", "cancer"])

def seine_count(text, lemmas):
    # return 1 if re.search(r"\bSeine\b", text) is not None else 0
    return len(re.findall(r"\bSeine\b", text))



# def korea_count(text, lemmas):
#     return 1 if "Corée" in lemmas else 0

# def not_usa_count(text, lemmas):
#     return 1 if not any(re.match("[EÉ]tats-Unis", lemma) for lemma in lemmas) else 0

# def seine_count(text, lemmas):
#     return 1 if re.search(r"\bSeine\b", text) is not None else 0

# def not_trump_count(text, lemmas):
#     return 1 if re.search(r"\bTRUMP\b", text) is None else 0

# def not_russia_count(text, lemmas):
#     return 1 if "Russie" not in lemmas else 0

# def russia_count(text, lemmas):
#     return 1 if "Russie" in lemmas else 0

# def korea_count(text, lemmas):
#     return 1 if "Corée" in lemmas else 0

# def china_count(text, lemmas):
#     return 1 if "Chine" in lemmas else 0

# def war_count(text, lemmas):
#     return 1 if "guerre" in lemmas else 0

# def washington_count(text, lemmas):
#     return 1 if "Washington" in lemmas else 0

# def not_war_count(text, lemmas):
#     return 1 if "guerre" not in lemmas else 0

# def ordonnance_count(text, lemmas):
#     return 1 if "ordonnance" in lemmas else 0

# def parliament_count(text, lemmas):
#     return 1 if re.search(r"\bParlement\b", text) is not None else 0

# def law_count(text, lemmas):
#     return 1 if "loi" in lemmas else 0

# def research_count(text, lemmas):
#     return 1 if "recherche" in lemmas else 0

# def regression_count(text, lemmas):
#     return 1 if any(re.match("r[eé]gression", lemma) for lemma in lemmas) else 0

# def police_count(text, lemmas):
#     return 1 if "police" in lemmas else 0

# def sunday_count(text, lemmas):
#     return 1 if "dimanche" in lemmas else 0