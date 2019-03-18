import xml.etree.ElementTree as ET
import sys

# class_doc = ["immobilier",
#              "travail",
#              "personne et famille",
#              "finances, fiscalité et assurance",
#              "rapport à la société",
#              "monde da la justice",
#              "entreprise",
#              "internet,téléphonie et prop. intellectuelle"]
#
# doc_size = [3788, 2468, 2010, 1118, 1413, 994, 498, 269]

def main():
    # class_mapping = defaultdict()
    with open(sys.argv[1], 'r', encoding='utf-8') as xml_file:
        tree = ET.parse(xml_file)
        new_tree = ET.Element('corpus')
        corpus = tree.getroot()
        counter = 1
        for doc in corpus:
            if counter%10 == 1:
                new_tree.append(doc)
            counter += 1
    ET.ElementTree(new_tree).write(sys.argv[2], encoding='utf-8',
                                       xml_declaration=True)


if __name__ == '__main__':
    main()