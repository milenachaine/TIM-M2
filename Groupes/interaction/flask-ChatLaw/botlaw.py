# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template, abort, jsonify
import uuid
from bold import * 

app = Flask(__name__)

""" Un dictionnaire 
{id_de_conversation_1 : [(locuteur, replique),(locuteur, replique), (locuteur, replique)],
id_de_conversation_2 : [(locuteur, replique),(locuteur, replique)], 
...}
"""
discussions = {}
dicoTerms = constructDico('list_terms.txt')

@app.route("/", methods=['GET', 'POST'])
def index():
	#NB : le premier chargement de la page se fait en GET, on ne rentre dans ce if qu'avec l'envoi du 1er message
	if request.method == "POST":
		#Vérification de la bonne formation du message reçu (du json avec un champs 'message' non-vide et un id de conversation)
		if not request.json or not 'message' in request.json or not request.json['message'] or not 'convID' in request.json:
			#On plante si le message est mal formé
			abort(400)

		#Sinon on récupère l'id de conversation et le message
		convID = request.json['convID']
		msg = request.json['message']
		#On note la nouvelle réplique dans les logs du serveurs
		discussions.setdefault(convID, [])
		discussions[convID].append( ("user", msg) )
		
		"""fonction Boyu pour enrichir msg"""
		msg = bold(msg, dicoTerms)
		
		# La gestion du schéma d'interraction goes here
		return jsonify({"messageB": "J'ai bien reçu le message", "messageU": msg}), 201

	return render_template("chatlaw.html", convID=uuid.uuid4()), 200

if __name__ == "__main__":
	app.run(debug=True)
