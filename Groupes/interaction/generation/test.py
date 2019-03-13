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
		logs.append( ("user", str(request.form['text'])) )
	
	return render_template("chatroom.html", discussion = logs)
	# Possibilité de récupérer soit en POST soit en Ajax.


	
if __name__ == '__main__':
	app.run()#Lance le serveur