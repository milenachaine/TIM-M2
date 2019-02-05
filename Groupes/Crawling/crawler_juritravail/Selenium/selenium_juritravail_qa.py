from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import unidecode

driver = webdriver.Firefox()
site = "juritravail"

# attendre 10s au maximum avant de récupérer les éléments
driver.implicitly_wait(10)

try:

	driver.get("https://www.juritravail.com/forum-juridique")

	# Création de la liste de catégories de la page principale https://www.juritravail.com/forum-juridique (27 catégories)
	
	cat_list = []
	resultats = driver.find_elements_by_xpath("//span[contains(@class, 'jt-inlineBloc floatLeft')]//a")
	for resultat in resultats:
		cat_list.append(resultat.text)
		print(resultat.text)
	#print(cat_list)
	
	# Parcours des catégories et création de listes de sous-catégories
	
	for elem in cat_list:
		categorie = driver.find_element_by_link_text(elem)
		categorie.click()
		resultats = driver.find_elements_by_xpath("//span[contains(@class, 'puceTriangleGris jt-inlineBloc')]//a")
		
		subcat_list = []
		for resultat in resultats:
			subcat_list.append(resultat.text)
			print(elem,".",resultat.text)		
		subject_list = []
		
		# S'il n'existe pas de sous-catégories dans subcat_list
		if not subcat_list:
		
			print("Pas de sous-catégorie")
			print(driver.current_url)
			
			resultats = driver.find_elements_by_xpath("//td[contains(@class, 'colSujet')]//a//strong")
			for resultat in resultats:
				subject_list.append(resultat.text)
			#print(subject_list)
			
			i = 1
			for subject in subject_list:
				subject = driver.find_element_by_link_text(subject)
				subject.click()
				#print(driver.current_url)
				extract_title = driver.find_elements_by_xpath("//h1")
				titre = extract_title[1].text
				url = driver.current_url
				cat = str(elem)
				id = str(elem[0])+str(elem[1])+str(elem[2])+str(i)
				print("<doc class=\"{cat}\" id=\"{id}\" source=\"{site}\" titre=\"{titre}\" url=\"{url}\">".format(id=id, cat=cat, site=site, titre=titre, url=url))
				
				# Récupération de la question
				
				questions = driver.find_elements_by_xpath("//div[contains(@class, 'floatLeft commentContainer')]//div")
				question = questions[0].text	
				paragraphs = driver.find_elements_by_xpath("//div[contains(@class, 'floatLeft commentContainer')]//p[2]")
				if paragraphs:
					paragraph = paragraphs[0].text
					print("<question>{question}\n{paragraph}</question>".format(question=question, paragraph=paragraph))
				else:
					print(question)
					
				# Récupération des réponses
				
				reponses = driver.find_elements_by_xpath("//span[contains(@class, 'grade stars-10')]/../../div[1]/div/div[contains(@class, 'msg')]//div")
				#/../..//div[contains(@class, 'msg')]//div")
				if reponses:
					for reponse in reponses:
						reponse = reponse.text
						print("<answer>{reponse}</answer>".format(reponse=reponse))
				
				print("</doc>")
				i += 1
				driver.back()
			
			subject_list = []
		
		# S'il existe des sous-catégories dans subcat_list
		else:
			pass
			# for subcat in subcat_list:
				# print(driver.current_url)
				# try:
					# categorie = driver.find_element_by_link_text(subcat)

					# categorie.click()
					# print(driver.current_url)
					# resultats = driver.find_elements_by_xpath("//td[contains(@class, 'colSujet')]//a//strong")
					# print(resultats)
					
					# if resultats:
						# for resultat in resultats:
							# subject_list.append(resultat.text)
						# print(subject_list)
						
						
						
						# subject_list = []
					# else:						
						# print("catégorie vide")
						# subject_list = []
				
				# except:
					# print(subcat, "inaccessible")
					# pass
					
				# driver.back()
				

		driver.back()


finally:
	driver.quit()
	
