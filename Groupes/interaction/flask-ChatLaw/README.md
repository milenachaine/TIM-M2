Utilisation : 
- se placer dans Ajax_based 
- python3 chatlaw.py
ATTENTION : toute modification du css n'entrera en vigueur qu'une fois le serveur et le navigateur rebooté


Proposition schéma type interaction 
	1) Salutation, embrayage sur la demande de question
		Question utilisateur

	2) Demande de confirmation de la bonne détection de l'intention -> Boutons ?
			Reponse Négative => Demande de reformulation et boucle (3x max) jusqu'à avoir compris
			Reponse Positive -> Génération de la réponse

	3) Demande si la réponse est satisfaisante 
		Reponse positive -> fin de l'interaction
		Reponse négative -> retour au début