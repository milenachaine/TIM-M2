import glob

rep = glob.glob('/Users/duhayon-fontaine/iCloud_Drive_archive/Documents/notes-M2/m2_exo/s1/stat/TIM-M2/Groupes/Pretraitement/Corpus/*/*/*/*.conllu')

s = ""
for fic in rep:
    if "a" in fic:
        print(fic)
        doc = open(fic, 'r')

        obj = doc.read().split('\t')
        obj = obj[1:4]

        s = obj[0]+"/"+obj[1]+"/"+obj[2]

        print(s)
