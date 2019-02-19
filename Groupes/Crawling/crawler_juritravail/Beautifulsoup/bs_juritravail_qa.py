import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
from bs4 import BeautifulSoup
import math
import time
import unidecode
import re

site = "juritravail"

def string2id(string):
	split_string = string.split(" ")
	string_id = ""
	for part in split_string:
		if len(part) > 1:
			if part[0].isalpha() and part[1].isalpha():
				string_id = string_id + part[0] + part[1]
	return string_id

def download(url, user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0', num_retries = 1, charset='utf-8'):
	print ('Downloading: ', url)
	request = urllib.request.Request(url)
	request.add_header('User-Agent', user_agent)
	try:
		resp = urllib.request.urlopen(request)
		encoding = resp.headers.get_content_charset()
		if not encoding:
			encoding = chardet.detect(resp.read())['encoding']
		html = resp.read().decode(encoding)
	except (URLError, HTTPError, ContentTooShortError) as e:
		print ('Download error:', e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				return download(url, num_retries - 1) 
	return html
	
def get_nav_max(Url):
	try:
		nav_max = int(Url.find_all('a', attrs={'class':'paginate'})[-1].text)
	except:
		nav_max = 1	
	if nav_max == 1:
		try:
			nav_max = int(Url.find_all('a', attrs={'class':'paginate'})[-2].text)
		except:
			nav_max = 1
	return nav_max

def topic(topicUrl, path, theme):
	topicFrontPage = download("https://www.juritravail.com" + topicUrl)
	topicFrontPageSoup = BeautifulSoup(topicFrontPage, "html.parser")
	url = "https://www.juritravail.com" + topicUrl
	
	subcats = topicFrontPageSoup.find_all('span', attrs={'class':'puceTriangleGris jt-inlineBloc'})
	
	if subcats != []:
		for subcat in subcats:
			try:
				subtopic(subcat.a['href'], path, subcat.text, theme)
			except:
				continue
	else:
		nav_max = get_nav_max(topicFrontPageSoup)
		counter = 0
		
		for nav_page in range(1, nav_max+1):
			topicFrontPage = download("https://www.juritravail.com" + topicUrl + "/page/" + str(nav_page))
			topicFrontPageSoup = BeautifulSoup(topicFrontPage, "html.parser")
			
			for entry in topicFrontPageSoup.find_all('td', attrs={'class':'colSujet'}):
				counter += 1
				try:
					subcat = "xx"
					page(entry.a['href'], path, entry.text, subcat, theme, url, counter)
				except:
					continue

def subtopic(subtopicUrl, path, subcat, theme):
	subtopicFrontPage = download("https://www.juritravail.com" + subtopicUrl)
	subtopicFrontPageSoup = BeautifulSoup(subtopicFrontPage, "html.parser")
	url = "https://www.juritravail.com" + subtopicUrl
	
	nav_max = get_nav_max(subtopicFrontPageSoup)
	counter = 0
	
	for nav_page in range(1, nav_max+1):
		subtopicFrontPage = download("https://www.juritravail.com" + subtopicUrl + "/page/" + str(nav_page))
		subtopicFrontPageSoup = BeautifulSoup(subtopicFrontPage, "html.parser")

		for entry in subtopicFrontPageSoup.find_all('td', attrs={'class':'colSujet'}):
			counter += 1
			try:
				page(entry.a['href'], path, entry.text, subcat, theme, url, counter)
			except:
				continue
				
def page(entryUrl, path, entry, subcat, theme, url, counter):
	entryFrontPage = download(entryUrl)
	entryFrontPageSoup = BeautifulSoup(entryFrontPage, "html.parser")
	
	# ===== Début du document ===== #	
	
	# Récupération des métadonnées
	
	title = re.sub(r'\n\n', "", entry)
	subcat = unidecode.unidecode(string2id(re.sub(r' \([^\)]+\)$', "", subcat)))
	theme = unidecode.unidecode(string2id(re.sub(r' \([^\)]+\)$', "", theme)))
	id = (theme + "-" + subcat + str(counter))
	
	# Impression des métadonnées
	
	f = open(path, 'a')
	f.write("<doc class=\"" + theme + "\" subclass=\"" + subcat + "\" id=\"" + id + "\" source=\"juritravail\" title=\"" + title + "\" url=\"" + entryUrl + "\">\n")
	f.close()
	
	# Récupération de la question
	
	question = entryFrontPageSoup.find_all('div', attrs={'class':'floatLeft commentContainer'})[0]
	question = question.get_text().strip()
	question = re.sub(r'[^\t]+(\t)+\n[^\s]+\s[^\n]+\n\n', "", question)
	question = re.sub(r'\n+', "\n", question, flags=re.M)
	question = re.sub(r' +', " ", question)
	question = question.strip()
	
	# Impression de la question
	
	f = open(path, 'a')
	f.write("<question>\n" + question + "\n</question>\n")
	f.close()
	
	# Récupération des réponses
	
	answers = entryFrontPageSoup.find_all('div', attrs={'class':'floatLeft commentContainer'})[1:]
	for answer in answers:
		grade = answer.find_all('span', attrs={'class':'grade stars-10'})
		if grade != []:
			answer = answer.get_text().strip()
			answer = re.sub(r'[^\t]+(\t)+\n[^\s]+\s[^\n]+\n\n', "", answer)
			answer = re.sub(r'\+[^\n]+messages\n', "", answer)
			answer = re.sub(r'Répondre(.|\n)*', "", answer, flags=re.M)
			answer = re.sub(r'Signaler(.|\n)*', "", answer, flags=re.M)
			answer = re.sub(r'\n+', "\n", answer, flags=re.M)
			answer = re.sub(r' +', " ", answer)
			answer = answer.strip()
			
			# Impression de la réponse
			
			f = open(path, 'a')
			f.write("<answer>\n" + answer + "\n</answer>\n")
			f.close()
			
		else:
			continue
	
	f = open(path, 'a')
	f.write("</doc>\n")
	f.close()

	# ===== Fin du document ===== #	

def mainPage(mainUrl, path):
	main = download(mainUrl)
	mainSoup = BeautifulSoup(main, "html.parser")
	
	# ===== Début du corpus ===== #
	
	f = open(path, 'a')
	f.write("<corpus>\n")
	f.close()
	
	for theme in mainSoup.find_all('span', attrs={'class':'jt-inlineBloc floatLeft'}):
		try:
			topic(theme.a['href'], path, theme.text)
		except:
			continue
	
	f = open(path, 'a')
	f.write("</corpus>\n")
	f.close()
	
	# ===== Fin du corpus ===== #

if __name__ == "__main__":
	mainPage("https://www.juritravail.com/forum-juridique", "out.xml")