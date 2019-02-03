from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import unidecode

driver = webdriver.Firefox()

# attendre 10s au maximum avant de récupérer les éléments
driver.implicitly_wait(10)

def string2id(string):
	split_string = string.split(" ")
	string_id = ""
	for part in split_string:
		if len(part) > 1:
			if part[0].isalpha() and part[1].isalpha():
				string_id = string_id + part[0] + part[1]
	return string_id

try:

	driver.get("https://www.juritravail.com/forum-juridique")
	
	# Création de la liste de catégories de la page principale https://www.juritravail.com/forum-juridique (27 catégories)
	
	print("#"*5, "MAIN CATEGORIES","#"*5, "\n")
	
	cat_list = []
	iter = 0
	resultats = driver.find_elements_by_xpath("//span[contains(@class, 'jt-inlineBloc floatLeft')]//a")
	number_list = driver.find_elements_by_xpath("//span[contains(@class, 'nbForum')]")
	for resultat in resultats:
		cat_list.append(resultat.text)
		
		id = unidecode.unidecode(string2id(resultat.text))
		cat = resultat.text
		number = number_list[iter].text
		iter += 1
		
		print(id, ";", cat, ";", number)
	
	# Parcours des catégories et création de listes de sous-catégories
	
	print("\n", "#"*5, "SUB-CATEGORIES","#"*5, "\n")
	
	for elem in cat_list:
		categorie = driver.find_element_by_link_text(elem)
		categorie.click()
		resultats = driver.find_elements_by_xpath("//span[contains(@class, 'puceTriangleGris jt-inlineBloc')]//a")
		number_list = driver.find_elements_by_xpath("//span[contains(@class, 'nbMessagess')]")
		
		subcat_list = []
		iter = 0
		if resultats:
			for sous_cat in resultats:

				id = unidecode.unidecode(string2id(elem) + "-" + string2id(sous_cat.text))
				cat = elem + "." + sous_cat.text
				number = number_list[iter].text
				iter += 1
				
				print(id, ";", cat, ";", number)
		
			print("")
		driver.back()

finally:
	driver.quit()
	
