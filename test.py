import requests
from bs4 import BeautifulSoup
from imdb import IMDb
import csv
import pandas as pd
# rows = []
# ia = IMDb()
# top250 = ia.get_top250_movies()
# for index, movie in enumerate(top250[:]):
# 	print(index,movie.movieID)

df = pd.read_csv("test3.csv",encoding="utf-8")
print(df)
