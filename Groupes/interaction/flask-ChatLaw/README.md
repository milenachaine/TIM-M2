Utilisation en local : 
	- python3 botlaw.py
	Suivre le lien donné
	Les logs d'erreur s'affichent en fenêtre de commande

Utilisation sur le serveur :
	http://helium.lab.parisdescartes.fr:2252/chatlaw

Mettre à jour sur le serveur : 
	- ssh -l teamlaw -p 2251 helium.lab.parisdescartes.fr
	Se placer dans le repertoire adéquat
	- git pull
	On reboot le serveur pour que les changements entrent en effet 
		- sudo service apache2 restart 
	Les logs d'erreur sont à 
		- sudo less /var/log/apache2/error.log
Envoi / réception de fichiers par SCP (via SSH)
$ scp -P 2251 envoi.txt helium.lab.parisdescartes.fr:~/nomdistant.txt
$ scp -P 2251 helium.lab.parisdescartes.fr:~/nomdistant.txt recu.txt


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