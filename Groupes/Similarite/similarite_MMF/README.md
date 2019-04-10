# Travail de recherche sur la similarité

## Scripts de parcours :
 - parcourir le corpus prétraité (arborescence de fichiers CONLL) et le transformer en une dataframe Pandas (id + lemmes + POS + mots)
 - utilisation : `python3 01_parcours.py dossier-contenant-le-corpus`
 - /!\ c'est très long, mieux vaut récupérer la dataframe sur le serveur
 - **commande** : `scp -r -P 2251 teamlaw@helium.lab.parisdescartes.fr:git-TIM-M2/Groupes/Similarite/similarite_MMF/corpuspd.pkl mon-dossier`
## Scripts de calcul de similarité :
 - à partir de cette dataframe, on utilise scikit-learn pour calculer les poids tf-idf du corpus
 - puis on prétraite et on calcule les poids de la question de l'utilisateur, avant de renvoyer les réponses les plus proches d'après trois mesures de similarité : Cosinus, Euclidean, Manhattan
 - l'objectif étant de confirmer que la similarité Cosinus était bien la meilleure à utiliser pour l'interface
 - utilisation : `python3 02_tfidf.py dataframe-du-corpus`
 - et : `python3 03_sim.py dataframe-du-corpus`
## Scripts de génération de texte :
 - utilise des chaînes de Markov pour générer des réponses
 - à partir des réponses à ces questions similaires, on génère une réponse automatique
 - utilisation : `python3 04_gen.py dataframe-du-corpus chemin-vers-corpus-conll`
