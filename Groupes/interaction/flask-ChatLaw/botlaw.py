# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template, abort, jsonify
import uuid
import re
from bold import * 

app = Flask(__name__)

import os
path = os.path.dirname(os.path.realpath(__file__))+"/../../"

""" Un dictionnaire 
{id_de_conversation_1 : [(locuteur, replique),(locuteur, replique), (locuteur, replique)],
id_de_conversation_2 : [(locuteur, replique),(locuteur, replique)], 
...}
"""
discussions = {}
dicoTerms = constructDico(path+'/interaction/flask-ChatLaw/list_terms.txt')
#dicoTerms = constructDico('list_terms.txt')

@app.route("/", methods=['GET', 'POST'])
def index():
	#NB : le premier chargement de la page se fait en GET
	if request.method == "POST":
		#Vérification de la bonne formation du message reçu
		if not request.json or not 'message' in request.json or not request.json['message'] or not 'convID' in request.json:
			#On plante si le message est mal formé
			abort(400)

		#Sinon on récupère l'id de conversation et le message
		convID = request.json['convID']
		msg = request.json['message']
		#On note la nouvelle réplique dans les logs du serveurs
		discussions.setdefault(convID, [])
		discussions[convID].append( ("user", msg) )

		"""recherche de correspondance"""
		from test_question import getBestQuestion, predict
		juriClass = predict(path+'/categorisation/modelIrisLP.mdl', msg)
		bestQuestion = getBestQuestion(msg, juriClass)

		
		"""fonction Boyu pour enrichir msg"""
		#msg = bold(re.sub('\n', '</br>', msg), dicoTerms)
		question = bold(re.sub('\n', '</br>', bestQuestion['questions']), dicoTerms)
		reponse = bold(re.sub('\n', '</br>', bestQuestion['answers']), dicoTerms)

		#return jsonify({"messageU": msg, "juriClass": juriClass, "bestQuestion": question, "bestAnswer": reponse}), 201
		return jsonify({"juriClass": juriClass, "bestQuestion": question, "bestAnswer": reponse}), 201

	return render_template("chatlaw.html", convID=uuid.uuid4()), 200

if __name__ == "__main__":
	app.run(debug=True)
