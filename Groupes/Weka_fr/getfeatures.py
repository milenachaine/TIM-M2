#!/bin/env python3
# -*- coding: utf8 -*-

import re

# fake

def usa_count(text, lemmas):
    return 1 if re.search(r"\bUSA?\b", text) is not None else 0

def russia_count(text, lemmas):
    return 1 if "Russie" in lemmas else 0

def korea_count(text, lemmas):
    return 1 if "Corée" in lemmas else 0
	
def china_count(text, lemmas):
    return 1 if "Chine" in lemmas else 0
	
def war_count(text, lemmas):
    return 1 if re.search(r"\bwar\b", text, flags=re.IGNORECASE) is not None else 0
	
def washington_count(text, lemmas):
    return 1 if "Washington" in lemmas else 0
	
# parodic

def ordonnance_count(text, lemmas):
    return 1 if re.search(r"\bordonnances?\b", text, flags=re.IGNORECASE) is not None else 0
	
def parliament_count(text, lemmas):
    return 1 if re.search(r"\bParlement\b", text) is not None else 0

def law_count(text, lemmas):
    return 1 if re.search(r"\blois?\b", text, flags=re.IGNORECASE) is not None else 0

def research_count(text, lemmas):
    return 1 if re.search(r"\brecherches?\b", text, flags=re.IGNORECASE) is not None else 0
	
def ppronounI_count(text, lemmas):
    return 1 if re.search(r"\b[Jj]e\b", text) is not None else 0
	
# trusted
 
def disease_count(text, lemmas):
    return 1 if any(word in lemmas for word in ["tumeur", "cancer"]) else 0
	
def seine_count(text, lemmas):
    return 1 if re.search(r"\bseine\b", text, flags=re.IGNORECASE) is not None else 0
	
def regression_count(text, lemmas):
    return 1 if re.search(r"\br[ée]gression\b", text, flags=re.IGNORECASE) is not None else 0
	
def police_count(text, lemmas):
    return 1 if re.search(r"\bpolice\b", text, flags=re.IGNORECASE) is not None else 0

def sunday_count(text, lemmas):
    return 1 if re.search(r"\bdimanche\b", text, flags=re.IGNORECASE) is not None else 0
