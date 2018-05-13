#!/bin/env python3
# -*- coding: utf8 -*-

import sys
import xml.etree.ElementTree as ET

reload(sys)
sys.setdefaultencoding('utf8')

if len(sys.argv) < 2:
    print("usage: {} INPUT".format(sys.argv[0]))
    sys.exit()

xml_corpus = ET.parse(sys.argv[1])
root = xml_corpus.getroot()
i = 1

with open("all_lexico.txt", 'w') as f:
	for doc in root.findall("doc"):
		f.write("<category={}><article={}>\r\n".format(doc.get("class"), str(i)))
		text = doc.find("text").text.splitlines()
		f.write("\r\n".join([line.strip() for line in text if line]))
		i += 1