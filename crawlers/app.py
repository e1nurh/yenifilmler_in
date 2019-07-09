from datetime import timedelta
from crawlers import *
from celery import Celery
from celery.task import periodic_task

import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')


app = Celery('tasks', backend='amqp',
             broker='amqp://guest@localhost//')


@periodic_task(run_every=timedelta(seconds=15))
def a():
	print("calling fuctions...")
	print("HDFILMSIZLE starting...")
	try:
		h = HdFilmsIzle()
		h.getNewFilms()
		h.writeToTxt()
		print("HDFILMSIZLE finished!")
	except Exception as e:
		print(e)
	print("EKRANLARDAN starting...")
	try:
		e = Ekranlardan()
		e.getNewFilms()
		e.writeToTxt()
		print("EKRANLARDAN finished...")
	except Exception as e:
		print(e)
	print("UltraHdFilm starting...")
	try:
		h = UltraHdFilm()
		h.getNewFilms()
		h.writeToTxt()
		print("UltraHdFilm finished!")
	except Exception as e:
		print(e)
	print("FullHdFilmSitesi starting...")
	try:
		e = FullHdFilmSitesi()
		e.getNewFilms()
		e.writeToTxt()
		print("FullHdFilmSitesi finished...")
	except Exception as e:
		print(e)
	print("FilmIzleFilmSitesi starting...")
	try:
		h = FilmIzleFilmSitesi()
		h.getNewFilms()
		h.writeToTxt()
		print("FilmIzleFilmSitesi finished...")
	except Exception as e:
		print(e)

