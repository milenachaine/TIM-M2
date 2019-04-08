Travail pour effectuer les recherches de similarité directement sur le corpus prétraité + tester différents types de similarité + tester la génération de textes

## Scripts de parcours : parcourir le corpus prétraité et le transformer en une Dataframe Pandas (id + lemmes + POS + mots)
## Scripts de calcul de similarité : permet de comparer trois types de similarités sur les questions du corpus 

01_parcours.py attend le dossier de corpus et le transforme en dataframe
02_tfidf.py effectue l'essentiel du tf-idf et l'enregistre dans des pickles
03_sim.py permet de traiter une question et de renvoyer différentes similarités à partir de ces pickles
