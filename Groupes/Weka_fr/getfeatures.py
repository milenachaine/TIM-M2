#!/bin/env python3
# -*- coding: utf8 -*-

import re

def usa_count(text):
    return 1 if re.search(r"\bUSA?\b", text) is not None else 0

def russia_count(text):
    return 1 if re.search(r"\b[Rr]ussie\b", text) is not None else 0

def korea_count(text):
    return 1 if re.search(r"\b[Cc]orée\b", text) is not None else 0

def disease_count(text):
    return 1 if re.search(r"\btumeur|cancer\b", text, flags=re.IGNORECASE) is not None else 0
