#FLASK_APP=test.py flask run 
# OU 
#python3 test.py
from flask import Flask #importer flask
from flask import render_template
from flask import request 
#Instancier l'objet app : le site Web
app = Flask(__name__) 
app.debug = True #'False' A LA MISE EN LIGNE

logs = []

@app.route("/", methods=['GET', 'POST'])
def index():
	global logs
	"""Affiche l'historique de conversation et recueil les réponses"""
	if request.method == 'POST':
		message = str(request.form['text'])
		logs.append( ("user", message) )
		if message != "Fort Bien":
			#envoi le pré-traitement de la requête
			#lance le calcul de similarité (ou autre)
			reponse = "okay, j'ai reçu la description du problème.\nJ'y répond"
			#Ajoute la réponse
			logs.append( ("bot", reponse) )
			#Demande si cela convient en affichant des boutons
			#if bouton == oui :
				#bye bye
			#else : 
				#repart pour un tour
		
	
	return render_template("chatroom.html", discussion = logs)
	# Possibilité de récupérer soit en POST soit en Ajax.


	
if __name__ == '__main__':
	app.run()#Lance le serveur