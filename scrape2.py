import requests
from bs4 import BeautifulSoup
from imdb import IMDb
import csv
import pandas as pd
import pickle

# writer = csv.writer(open('test.csv','w'))
vars = ['ID','Title','Director','Rating','Year','Summary','Runtime',"Small_image","Big_image","Genre","Budget","Revenue"]
# writer.writerow(vars)

rows = []
ia = IMDb()

top250 = ia.get_top250_movies()
for index,movie in enumerate(top250):
	print(index,movie.movieID)
	url = 'http://www.imdb.com/title/tt'+movie.movieID
	page = requests.get(url).content
	soup = BeautifulSoup(page, 'html.parser')
	title = soup.select_one("#ratingWidget > p > strong").text
	# print(title)
	director = soup.select_one("span[itemprop=name]").text
	# print(director)
	rating = soup.select_one("span[itemprop=ratingValue]").text
	# print(rating)
	year = soup.select_one("meta[itemprop=datePublished]")['content'][:4]
	# print(year)
	summary = soup.select_one("div[itemprop=description]").text.strip()
	# print(summary)
	runtime = soup.select_one("time[itemprop=duration]").text.strip()
	# print(runtime)
	small_poster = soup.select_one(".poster > a > img")['src']
	# print(small_poster)
	big_poster = small_poster.split("@")[0] + "@._V1_SY1000_CR0,0,700,1000_AL_.jpg"
	# print(big_poster)
	genres = soup.select("span[itemprop=genre]")
	genre = ""
	for g in genres:
		genre += ", " + g.text 
	genre = genre[2:]
	# print(genre)
	try:
		bhead = soup.find(text="Budget:")
		btext = bhead.parent.parent.text.strip()
		budget = btext[7:].split("\n")[0]
	except:
		budget = "N/A"
	# print(budget)
	try:
		wgross = soup.find(text="Cumulative Worldwide Gross:").parent.parent.text.strip()
		# print(wgross)
		revenue = wgross[28:].split(", ")[0]
	except:
		try:
			usgross = soup.find(text="Gross USA:").parent.parent.text.strip()
			# print(usgross)
			revenue = usgross[11:].split(", ")[0]
		except:
			revenue = "N/A"
	# print(revenue)
	row = [movie.movieID,title,director,rating,year,summary,runtime,small_poster,big_poster,genre,budget,revenue]
	# writer.writerow(row)
	rows.append(row)
pickle.dump(rows, open( "save.p", "wb" ) )
df = pd.DataFrame(rows)
df.to_csv("test3.csv")