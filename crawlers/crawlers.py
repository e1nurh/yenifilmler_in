import requests
from bs4 import BeautifulSoup as bs
import json
import codecs


def hdfilmsizlesearch(word):
	film_details = []
	r = requests.get("https://www.hdfilmsizle2.com/?s="+word)
	b = bs(r.content, 'html.parser')
	film_list = b.find_all('div', {"class": "frag-k"})
	for i in film_list:
		film_detail = {}
		film_detail['title'] = i.find('a', {"class": "resim"}).get('title')
		film_detail['film_url'] = i.find('a', {"class": "resim"}).get('href')
		film_detail['poster'] = i.find('img').get('src')
		film_details.append(film_detail)
	return film_details

def ekranlardansearch(word):
	film_details = []
	r = requests.get("https://www.ekranlardan.com/?s="+word)
	b = bs(r.content, 'html.parser')
	film_list = b.find_all('div', {"class":"frag-k"})
	for i in film_list:
		film_detail = {}
		film_detail['title'] = i.find('a', {"class": "resim"}).get('title')
		film_detail['film_url'] = i.find('a', {"class": "resim"}).get('href')
		film_detail['poster'] = i.find('img').get('src')
		film_details.append(film_detail)
	return film_details


def ultrahdfilmsearch(word):
	film_details = []
	r = requests.get("https://www.ultrahdfilm.com/?s="+word)
	b = bs(r.content, 'html.parser')
	film_list = b.find_all('div', {"class":"movie-preview-content"})
	for i in film_list:
		film_detail = {}
		film_detail['title'] = i.find('span', {"class": "movie-title"}).find('a').get('title')
		film_detail['film_url'] = i.find('span', {"class": "movie-title"}).find('a').get('href')
		film_detail['poster'] = i.find('img').get('src')
		film_details.append(film_detail)
	return film_details

def fullhdfilmsitesisearch(word):
	film_details = []
	r = requests.get("https://www.fullhdfilmsitesi1.net/?arama="+word)
	b = bs(r.content, 'html.parser')
	film_list = b.find_all('div', {"class":"moviefilm"})
	for i in film_list:
		film_detail = {}
		film_detail['title'] = i.find('div', {"class": "movief"}).getText()
		film_detail['film_url'] = i.find('a').get('href')
		film_detail['poster'] = i.find('img').get('src')
		film_details.append(film_detail)
	return film_details

def filmizlefilmsitesisearch(word):
	film_details = []
	r = requests.get("https://www.filmizlefilmsitesi.com/?s="+word)
	b = bs(r.content, 'html.parser')
	film_list = b.find_all('div', {"class":"existing_item"})
	for i in film_list:
		film_detail = {}
		film_detail['title'] = i.find('div', {"class": "name"}).find('a').getText()
		film_detail['film_url'] = i.find('a').get('href')
		film_detail['poster'] = i.find('img').get('src')
		film_details.append(film_detail)
	return film_details

class HdFilmsIzle():
	def __init__(self):
		self.url = "https://www.hdfilmsizle2.com/"
		self.film_details = []
		self.result_file = 'hdfilmsizle.txt'

	def getNewFilms(self):
		r = requests.get(self.url)
		b = bs(r.content, 'html.parser')
		yeni_filmler_class = b.find('div', {"class": "son"})
		film_list = yeni_filmler_class.find_all('div', {"class": "frag-k"})
		for i in film_list:
			print("ok")
			film_detail = {}
			film_detail['title'] = i.find('a', {"class": "resim"}).get('title')
			film_detail['film_url'] = i.find('a', {"class": "resim"}).get('href')
			film_detail['poster'] = i.find('img').get('src')
			self.film_details.append(film_detail)

	def writeToTxt(self):
		with codecs.open(self.result_file, 'w', encoding='utf-8') as f:
			json.dump(self.film_details, f, ensure_ascii=False)


class Ekranlardan():
	def __init__(self):
		self.url = "https://www.ekranlardan.com/"
		self.film_details = []
		self.result_file = "ekranlardan.txt"

	def getNewFilms(self):
		r = requests.get(self.url)
		b = bs(r.content, 'html.parser')
		yeni_filmler_class = b.find('div', {"class": "son"})
		film_list = yeni_filmler_class.find_all('div', {"class":"frag-k"})
		for i in film_list:
			film_detail = {}
			film_detail['title'] = i.find('a', {"class": "resim"}).get('title')
			film_detail['film_url'] = i.find('a', {"class": "resim"}).get('href')
			film_detail['poster'] = i.find('img').get('data-src')
			self.film_details.append(film_detail)

	def writeToTxt(self):
		with codecs.open(self.result_file, 'w', encoding='utf-8') as f:
			json.dump(self.film_details, f, ensure_ascii=False)

class UltraHdFilm():
	def __init__(self):
		self.url = "https://www.ultrahdfilm.com/"
		self.film_details = []
		self.result_file = "ultrahdfilm.txt"

	def getNewFilms(self):
		r = requests.get(self.url)
		b = bs(r.content, 'html.parser')
		yeni_filmler_class = b.find('div', {"class": "fix-film-v2_item"})
		film_list = yeni_filmler_class.find_all('div', {"class":"movie-preview-content"})
		for i in film_list:
			film_detail = {}
			film_detail['title'] = i.find('span', {"class": "movie-title"}).find('a').get('title')
			film_detail['film_url'] = i.find('span', {"class": "movie-title"}).find('a').get('href')
			film_detail['poster'] = i.find('img').get('src')
			self.film_details.append(film_detail)

	def writeToTxt(self):
		with codecs.open(self.result_file, 'w', encoding='utf-8') as f:
			json.dump(self.film_details, f, ensure_ascii=False)

class FullHdFilmSitesi():
	def __init__(self):
		self.url = "https://www.fullhdfilmsitesi1.net/"
		self.film_details = []
		self.result_file = "fullhdfilmsitesi.txt"

	def getNewFilms(self):
		r = requests.get(self.url)
		b = bs(r.content, 'html.parser')
		film_list = b.find_all('div', {"class":"moviefilm"})
		for i in film_list:
			film_detail = {}
			film_detail['title'] = i.find('div', {"class": "movief"}).getText()
			film_detail['film_url'] = i.find('a').get('href')
			film_detail['poster'] = i.find('img').get('src')
			self.film_details.append(film_detail)

	def writeToTxt(self):
		with codecs.open(self.result_file, 'w', encoding='utf-8') as f:
			json.dump(self.film_details, f, ensure_ascii=False)

class FilmIzleFilmSitesi():
	def __init__(self):
		self.url = "https://www.filmizlefilmsitesi.com/"
		self.film_details = []
		self.result_file = "filmizlefilmsitesi.txt"

	def getNewFilms(self):
		r = requests.get(self.url)
		b = bs(r.content, 'html.parser')
		film_list = b.find_all('div', {"class":"existing_item"})
		for i in film_list:
			film_detail = {}
			film_detail['title'] = i.find('div', {"class": "name"}).find('a').getText()
			film_detail['film_url'] = i.find('a').get('href')
			film_detail['poster'] = i.find('img').get('src')
			self.film_details.append(film_detail)

	def writeToTxt(self):
		with codecs.open(self.result_file, 'w', encoding='utf-8') as f:
			json.dump(self.film_details, f, ensure_ascii=False)
