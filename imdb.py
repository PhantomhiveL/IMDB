#It needs the requests module
#Tested in Debian based distributions

#Modules
from requests import *
from color import *
import sys
import os
import json

os.system("clear")

#Class
class movie:
	#Initial
	def __init__(self):
		#Site
		self.site = "http://www.omdbapi.com/"
		
		#Search
		self.t = raw_input("Title: ")
		self.y = raw_input("Year: ")
		self.ty = raw_input("Type: ")


	def all(self):
		#No Title
		if self.t == "":
			print "No Title!"
			exit()

		#Get the information about the movie
		self.txt = get(self.site+"?t="+self.t+"&y="+self.y+"&type="+self.ty).text

	def info(self):
		os.system("clear")

		#Uses the function all
		self.all()

		#Convert to a dictionary
		self.txt = json.loads(self.txt)

		try:
			#Information about the movie
			title = self.txt["Title"]
			released = self.txt["Released"]
			genre = self.txt["Genre"]
			plot = self.txt["Plot"]
			runtime = self.txt["Runtime"]
			typee = self.txt["Type"]
			language = self.txt["Language"]
			country = self.txt["Country"]

			writer = self.txt["Writer"]
			director = self.txt["Director"]
			actors = self.txt["Actors"]
			production = self.txt["Production"]

			awards = self.txt["Awards"]

			imdbvotes = self.txt["imdbVotes"]
			imdbrating = self.txt["imdbRating"]

			#Prints the information 
			print blue("Title")+":", title
			print blue("Released")+":", released
			print blue("Genre")+":", genre
			print blue("Runtime")+":", runtime
			print blue("Type")+":", typee
			print blue("Language")+":", language
			print blue("Country")+":", country

			print "\n"+plot

			print "\nWriter:", writer
			print "Director:", director
			print "Actors:", actors
			print "Production:", production

			print "\nAwards:", awards

			print "\n"+yellow("IMDB Votes")+":", imdbvotes
			print yellow("IMDB Rating")+":", imdbrating

			print ""

			#Press Enter
			raw_input("")
		except:
			pass

#Object
F = movie()
F.info()
