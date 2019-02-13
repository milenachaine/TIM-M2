[13/02/19]
En cours : 
- réalisation d'un schéma d'interaction basique 
- étude du Framework Flask pour réalisr une interface web



[06/02/19]
Proposition schéma type interaction 
	1) Salutation, embrayage sur la demande de question
		Question utilisateur
			Identification de l'intention 
	2) Demande de confirmation de la bonne détection de l'intention
		Réponse
			Detection de l'intention
			Reponse Négative => Demande de reformulation et boucle (3x max) jusqu'à avoir compris
			Reponse Positive -> Génération de la réponse
	3) Demande si la réponse est satisfaisante 
		Reponse positive -> fin de l'interaction
		Reponse négative -> retour à la ligne 5
	
	
Méthodes Symbolique ou apprentissage ? N-grams
Génération de texte, ou juste proposition des réponses ?

Quelles entitées nommées ?

Quelle interface ? bot discord/slack/fb, fenetre de commande, web ?