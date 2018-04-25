#!/bin/env python3
# -*- coding: utf8 -*-

import re

def usa_count(text):
    return 1 if re.search(r"\bUSA?\b", text) is not None else 0

def russia_count(text):
    return 1 if re.search(r"\bRussie\b", text) is not None else 0