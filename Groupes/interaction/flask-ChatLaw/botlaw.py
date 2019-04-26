# -*- coding: UTF-8 -*-
import uuid
import re
import os
from flask import Flask, request, render_template, abort, jsonify
from bold import *
from test_question import getBestQuestion, predict
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


#On initialise l'application Flask
app = Flask(__name__)
#La variable qui adapte les chemins à l'architecture
path = os.path.dirname(os.path.realpath(__file__))+"/../../"

#Le dictionnaire pour enregistrer les logs (non-exploité)
discussions = {}
#Le dictionnaire nécéssaire au repérage des mots-clefs
dicoTerms = constructDico(path+'/interaction/flask-ChatLaw/list_terms.txt')
#Le dictionnaire qui associe l'identifiant d'une question son l'URL source
dictID_url = {}
#On le remplie
mydoc = ET.ElementTree(file= path + 'Crawling/corpusIrisVersion4.xml')
for e in mydoc.findall('.//doc'):
    dictID_url[e.get('id')] = e.get('url')

#Le dictionnaire qui permet d'afficher proprement le nom des classes
decode_classe = {
    "imm" : "immobilier",
    "trv" : "travail",
    "per" : "personne et famille",
    "fin" : "finances, fiscalité et assurance",
    "soc" : "rapports à la société",
    "jus" : "monde de la justice",
    "ent" : "entreprise",
    "int" : "internet, téléphonie et prop. intellectuelle"
}


@app.route("/", methods=['GET', 'POST'])
def index():
	#NB : le premier chargement de la page se fait en GET
	if request.method == "POST":
		#Vérification de la bonne formation du message reçu
		if not request.json or not 'message' in request.json or not request.json['message'] or not 'convID' in request.json:
			#Si le message est mal formé, on plante
			abort(400)

		#Sinon on récupère l'id de conversation et le message utilisateur
		convID = request.json['convID']
		msg = request.json['message']
		#On note la nouvelle réplique dans les logs du serveurs
		discussions.setdefault(convID, [])
		discussions[convID].append( ("user", msg) )

		"""Recherche de la classe la plus probable, 
		et de la question la plus similaire"""
		juriClass = predict(path+'/categorisation/modelIrisLP.mdl', msg)
		bestQuestion = getBestQuestion(msg, juriClass)
		#On récupère la question, sa réponse et l'URL source
		question = bestQuestion['questions']
		reponse = bestQuestion['answers']
		url = dictID_url[bestQuestion['id']]
		
		"""implémentation des balises nécéssaires 
		à la dissimulation d'une partie du texte """
		def cacherTexte(txt) : 
			mots = txt.split(' ')
			if len(mots)<30 :
				return txt
			else : 
				result = '<span class="teaser">'+' '.join(mots[:30])+'</span> '
				result = result + '<span class="complete">'+' '.join(mots[30:])+'</span>'
				result = result + '<span class="more"> Voir Plus</span>'
				return result
		question = cacherTexte(question)
		reponse = cacherTexte(reponse)

		
		"""Recherche des mots-clef"""
		question = bold(cut(re.sub('\n', '</br>', question), dicoTerms), dicoTerms)
		reponse = bold(cut(re.sub('\n', '</br>', reponse), dicoTerms), dicoTerms)
		
		# Envoi la réponse du serveur, en Json
		# (classe, question et reponse les +similaires, url)
		return jsonify({"juriClass": decode_classe[juriClass], "url": url, "bestQuestion": question, "bestAnswer": reponse}), 201

	return render_template("chatlaw.html", convID=uuid.uuid4()), 200

if __name__ == "__main__":
	app.run(debug=False) 
	#debug doit être false à la mise en prod.
