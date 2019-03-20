Les fichiers sorties en conll sont déjà stocké sur la machine à distance, pour les récupérer:

scp -P 2251 chuanming@helium.lab.parisdescartes.fr:pretraitement/juritravail votre_répertoir 

scp -P 2251 chuanming@helium.lab.parisdescartes.fr:pretraitement/net-iris votre_répertoir 

le mot de passe est: dcm

I.Construction de treebank

pour générer les fichier conll, vous devez d'abord installer treetagger et assurez que la commande "$tree-tagger-french" marche.

En suite, si vous êtes sous linux ou dispose un terminal linux, entrez:

python3 xml2conll.py chemin_relatif_de_fichier_xml chemin_relatif_de_dossier_cible

ex:
     vous êtes déjà dans un répertoire qui contient le dossier du projet TIM-M2, vous devez naturellement entrer
	 
	 python3 xml2conll.py TIM-M2/Croupes/Crawling/corpusIrisVersion4.xml TIM-M2/Groupes/Prétraitement/Corpus
	 
Si vous utilisez windows, remplacez tous les "/" dans la description de chemin dans xml2conllu.py par "\\", 
ex:
     mydir+"/"+cat+"/"+sub+"/"+ID => mydir+"\\"+cat+"\\"+sub+"\\"+ID

Cette procédure durera 3-4 heures, taille total 688MB, 
assurez que votre ordinateur aie assez de batterie et espace.

L'hiérarchie de dossier est 
Corpus/Nom_de_ressource/Nom_de_Classe/Nom_de_Sous-classe/Nom_de_Doc/fichier_question_et_réponse_avec_id_de_corpus_et_index_de_q_et_a 

Un autre script phrase2conll.py prend en argument une phrase et stocke le résultat de treetagger dans un fichier "phrase.conll", utilisation: $python phrase2conll.py "c'est un test" 

à part des fichiers conll, il produit aussi un fichier phrases.txt dans le dossier cible qui récolte tous les phrases dans les questions et réponses, segmentées par spacy, prêt pour extraction des entité nommées. 

II.Trouver les entités nommées

Vous devez installer polyglot et assurer que ça marche par tester 'downloader.download("embeddings2.fr")', si problème d'absence de module "icu", regardez 
https://markhneedham.com/blog/2017/11/28/python-polyglot-modulenotfounderror-no-module-named-icu/	 

Vous n'êtes pas recommandé d'exécuter ce script, parce que nous avons fait fonctionner polyglot pour chaque phrase segmentés par spacy pour obtenir une liste d'entité plus propre, ainsi cause un problème de la durée de traitement, cela m'a pris 8 heures pour finaliser l'extraction. Vous êtes conseillés de prendre directement le fichier déjà produit "ents.txt"

III.Trouver les mots juridiques

Nous avons testé deux approches pour extraire les mots juridiques, 

     1. TF-IDF. Pour ce faire nous avons récolté un corpus journaliste pour faire la contraste avec notre corpus juridique en retirant les mots qui a ont un score tfidf plus haut dans le corpus juridique. Regardez TFIDF.py. Les défauts sont évidentes, d'abord c'est pas facile de trouver les n-grammes juridiques; aussi, le genre et registre de corpus de contraste est très différent, par exemple, puisque le fichier contraste "contraste" ici est un corpus journaliste, alors il n'y a pas de mode en deuxième personne, ainsi beaucoup de conjugaison en deuxième personne dans le corpus juridique est prise en compte. Le résultat est stocké dans "jury.txt"

     2. A partir d'un dictionnaire juridique en ligne nous pouvons extraire la liste des termes juridique dans "termes_juridiques.txt", le script de téléchargement est "jury.py". A l'aide de cette liste nous pouvons récolter les termes juridiques bien propres depuis notre corpus. Le script est "extraction.py", et le résultat est "jury_words.txt"   

	 
