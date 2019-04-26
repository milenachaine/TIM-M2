Utilisation en local : 
	- python3 botlaw.py
	Suivre le lien donné
	Les logs d'erreur s'affichent en fenêtre de commande

Utilisation sur le serveur :
	- git pull
	On reboot le serveur pour que les changements entrent en effet 
		- sudo service apache2 restart
	On va sur http://helium.lab.parisdescartes.fr:2252/chatlaw
	Les logs d'erreur sont à 
		- sudo less /var/log/apache2/error.log


ARBORESCENCE :
- botlaw.py
	- le contenu du repertoire "static"
	- le contenu du repertoire "templates"
	- bold.py
		- list_terms.txt
	- test_question.py
		- make_prediction.py
			- corpus.py


ATTENTION : 
	- On ne modifie pas les fichiers directement sur le serveur
	- toute modification du css n'entrera en vigueur qu'une fois le cache du navigateur vidé