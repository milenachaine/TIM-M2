from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

# attendre 10s au maximum avant de récupérer les éléments
driver.implicitly_wait(10)

try:


	driver.get("https://www.juritravail.com/forum-juridique")

	# categorie = driver.find_element_by_link_text("Loi travail 2017")
	# categorie.click()
	
	# click sur le champ depart
	# depart = driver.find_element_by_css_selector("div.gws-flights-form__input-container:nth-child(1)")
	# depart.click()

	# selection de l'aeroport de depart (tous les aeroport de paris)
	# paris = driver.find_element_by_css_selector(".fsapp-option-city-name")
	# paris.click()
	# time.sleep(1)

	# click sur le champ arrivee
	# arrivee = driver.find_element_by_css_selector("div.gws-flights-form__input-container:nth-child(3)")
	# arrivee.click()

	# trouver le champ de saisie de l'arrivee
	# saisie_arrivee = driver.find_element_by_css_selector("input[placeholder]")
	# saisie_arrivee.send_keys("USA")
	
	# selection du pays d'arrivee
	# usa = driver.find_element_by_css_selector(".fsapp-option-city-name")
	# usa.click()
	# time.sleep(1)

	# lancer la recherche
	# recherche = driver.find_element_by_css_selector(".gws-flights-form__search-button")
	# recherche.click()
	# time.sleep(5)

	# afficher les resultats
	cat_list = []
	resultats = driver.find_elements_by_xpath("//span[contains(@class, 'jt-inlineBloc floatLeft')]//a")
	for resultat in resultats:
		cat_list.append(resultat.text)
	#print(cat_list)
	
	for elem in cat_list:
		categorie = driver.find_element_by_link_text(elem)
		categorie.click()
		resultats = driver.find_elements_by_xpath("//span[contains(@class, 'puceTriangleGris jt-inlineBloc')]//a")
		
		subcat_list = []
		for resultat in resultats:
			subcat_list.append(resultat.text)
		
		subject_list = []
		if not subcat_list:
			resultats = driver.find_elements_by_xpath("//td[contains(@class, 'colSujet')]//a")
				for resultat in resultats:
					#subject_list.append(resultat.text)
		# on reparcoure la subcat_list
		#	on parcoure les pages finales (faire fonction)
		driver.back()


finally:
	driver.quit()
	
