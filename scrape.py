from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()
print(ia.get_movie_infoset())
# top250 = ia.get_top250_movies()
# for movie in top250:
# 	try:
# 		ia.update(movie,'main')
# 		print(movie.movieID)
# 	except:
# 		pass
s_result = ia.search_movie("Singin' in the Rain")
movie = s_result[0]
ia.update(movie,'main')
ia.update(movie,'plot')
ia.update(movie,'awards')
print(movie.keys())
print(movie['long imdb title'])
# print(movie['director'][0])
print(movie['genres'])
print(movie['runtimes'])
print(movie['year'])
print(movie['rating'])
print(movie['top 250 rank'])
print(movie['full-size cover url'])
print(movie['plot outline'])
print(movie['gross'])
