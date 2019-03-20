# coding: utf-8
#FLASK_APP=botlaw.py flask run 
# OU 
#python3 botlaw.py
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
		message = request.form['text']
		logs.append( ("user", message) )
		if message != "Fort Bien":
			#envoi le pré-traitement de la requête
			#lance le calcul de similarité (ou autre)
			# reponse = "NOPE, je boude, je fais grêve, j'ai mal aux pieds"
                        reponse = "coucou"
			#Ajoute la réponse
			logs.append( ("bot", reponse) )
			#Demande si cela convient
			#Affiche des boutons
			#if oui :
				#bye bye
			#if non :
				#
		
	
	return render_template("chatroom.html", discussion = logs)
	# Possibilité de récupérer soit en POST soit en Ajax.


	
if __name__ == '__main__':
	app.run()#Lance le serveur
