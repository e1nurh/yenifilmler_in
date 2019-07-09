from django.shortcuts import render, redirect
import json
from crawlers.crawlers import *

films_txt_list = [
	'ekranlardan.txt',
	'filmizlefilmsitesi.txt',
	'fullhdfilmsitesi.txt',
	'hdfilmsizle.txt',
	'ultrahdfilm.txt'
]


def get_films():
	film_list = {}
	for i in films_txt_list:
		with open('crawlers/'+i, 'r', encoding='utf-8') as f:
			films = json.loads(f.read())
			film_list[i[:-4]] = films
	return film_list

def home(request):
	films = get_films()
	content = {'films':films}
	return render(request, 'index.html', content)

def search(request):
	if request.method == "POST":
		word = request.POST.get("search_field")
		hdfilmsizle = hdfilmsizlesearch(word)
		ekranlardan = ekranlardansearch(word)
		ultrahdfilm = ultrahdfilmsearch(word)
		fullhdfilmsitesi = fullhdfilmsitesisearch(word)
		filmizlefilmsitesi = filmizlefilmsitesisearch(word)
		content = {
			"films": {
				"hdfilmsizle": hdfilmsizle,
				"ekranlardan": ekranlardan,
				"ultrahdfilm": ultrahdfilm,
				"fullhdfilmsitesi": fullhdfilmsitesi,
				"filmizlefilmsitesi": filmizlefilmsitesi
			}
		}
		return render(request, 'results.html', content)
	else:
		return redirect("/")