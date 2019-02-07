import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
from bs4 import BeautifulSoup
import math
import time

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

def entry(url, path, c = "unknown"):
	f = open(path, 'a')
	
	htmlFirstPage = download(url)
	if htmlFirstPage:
		soupFP = BeautifulSoup(htmlFirstPage, "html.parser")
	else:
		return 1
	
	title = (soupFP.h1.text.strip()).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", "&apos;")
	
	global counterDoc
	counterDoc += 1
	
	f.write('<doc class="' + c + '" id="iris' + str(counterDoc) +'" source="net-iris"' + ' url="' + url + '" title="' + title + '">\n')
	
	numberOfPosts = int(soupFP.find('div', attrs={'id':'postpagestats_above'}).text.split()[-1])

	numberOfPages = math.ceil(numberOfPosts / 12)
	
	posts = soupFP.find_all('li', attrs={'class':'postbitlegacy postbitim postcontainer'})
	
	askerName = posts[0].find('div', attrs={'class':'username_container'}).text.strip()
	
	idQa = 0 #Identification question-réponse
	
	for post in posts:
		if post.find('div', attrs={'class':'username_container'}).text.strip() == askerName:
			idQa += 1
			f.write("<question number=\"" + str(idQa) + "\">\n")
			contentLines = post.blockquote.find_all(text=True, recursive=False)
			for line in contentLines:
				if line != ' ':
					try:
						l = (line.strip()).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", "&apos;")
						f.write(l)
					except:
						continue
			f.write("\n</question>\n")
		else:
			f.write("<answer number=\"" + str(idQa) + "\">\n")
			contentLines = post.blockquote.find_all(text=True, recursive=False)
			for line in contentLines:
				if line != ' ':
					try:
						l = (line.strip()).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", "&apos;")
						f.write(l)
					except:
						continue
			f.write("\n</answer>\n")
			
	pageCounter = 1
	while pageCounter < numberOfPages:
		time.sleep(1)
		pageCounter += 1
		html = download(url[:-5] + "-" + str(pageCounter) + ".html")
		if html:
			soup = BeautifulSoup(html, "html.parser")
		else:
			return 1
		
		posts = soup.find_all('li', attrs={'class':'postbitlegacy postbitim postcontainer'})
		for post in posts:
			if post.find('div', attrs={'class':'username_container'}).text.strip() == askerName:
				idQa += 1
				f.write("<question number=\"" + str(idQa) + "\">\n")
				contentLines = post.blockquote.find_all(text=True, recursive=False)
				for line in contentLines:
					if line != ' ':
						try:
							l = (line.strip()).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", "&apos;")
							f.write(l)
						except:
							continue
				f.write("\n</question>\n")
			else:
				f.write("<answer number=\"" + str(idQa) + "\">\n")
				contentLines = post.blockquote.find_all(text=True, recursive=False)
				for line in contentLines:
					if line != ' ':
						try:
							l = (line.strip()).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", "&apos;")
							f.write(l)
						except:
							continue
				f.write("\n</answer>\n")
	f.write("\n</doc>\n")
	f.close()
	
def topic(topicUrl, path, c = "unknown"):
	topicFrontPage = download(topicUrl)
	topicFrontPageSoup = BeautifulSoup(topicFrontPage, "html.parser")
	topicNumberOfDiscussions = int(topicFrontPageSoup.find('div', attrs={"id":"threadpagestats"}).text.split()[-1])
	topicNumberOfPages = math.ceil(topicNumberOfDiscussions / 20)
	
	for discussion in topicFrontPageSoup.find_all('a', attrs={"class":"title"}):
		try:
			discussionHtml = discussion['href']
			entry(discussionHtml, path, c)
		except:
			continue
		
	topicCounter = 1
	while topicCounter < topicNumberOfPages:
		topicCounter += 1
		topicPage = download(topicUrl + "index" + str(topicCounter) + ".html")
		topicPageSoup = BeautifulSoup(topicPage, "html.parser")
		for discussion in topicPageSoup.find_all('a', attrs={"class":"title"}):
			try:
				discussionHtml = discussion['href']
				entry(discussionHtml, path, c)
			except:
				continue
			
def mainPage(mainUrl, path):
	main = download(mainUrl)
	mainSoup = BeautifulSoup(main, "html.parser")
	f = open(path, 'a')
	f.write("<corpus>\n")
	f.close()
	
	for theme in mainSoup.find_all('h2', attrs={'class':'forumtitle'})[:-3]:
		try:
			topic(theme.a['href'], path, theme.text)
		except:
			continue
	
	f = open(path, 'a')
	f.write("\n</corpus>\n")
	f.close()

if __name__ == "__main__":
	counterDoc = 0
	mainPage("https://forum-juridique.net-iris.fr", "out6.xml")



















