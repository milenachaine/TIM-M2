def interaction_type():
# 1) Salutation, embrayage sur la demande de question
question = input("Bonjour\n!Je suis le chatbot juridique de la promo IM 2018-2019, expliquez moi votre problème\n")
# Identification de l'intention

print("Je dispose de cette question dans ma base de données")
#print(suggestion)
confirmation = input("Cela correspond-t-il à ce que vous recherchez ?\n")
# Identification de l'intention

i=0
while i<3:
	if confirmation=True:
		break
	else:
		question = input("Alors réexpliquez moi s'il vous plait\n")
		pass

if confirmation = True:
	#génération de la réponse
	
else:
	print("Je suis désolé, je ne suis pas qualifié pour vous répondre.")
	print("Vous pouvez contacter un de nos conseillés humains au 01 01 01 01 01")
	