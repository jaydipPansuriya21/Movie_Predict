import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(index):
	return df[df.index==index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title==title]["index"].values[0]	


df = pd.read_csv("movie_dataset.csv")
#print df.columns

features = ['keywords','cast','genres','director']


for f in features:
	df[f] = df[f].fillna('')     

def combine_features(row):
	try:
		 return row['keywords'] +" "+row['cast'] +" "+row['genres'] +" "+row['director']
	except:
		print "Error : ",row



df["combine_features"] = df.apply(combine_features,axis=1)
cv = CountVectorizer()
count_metrix = cv.fit_transform(df["combine_features"])
cosine_sim = cosine_similarity(count_metrix)

movie_user_likes = "Avatar"
movie_index = get_index_from_title(movie_user_likes)

similar_movie = list(enumerate(cosine_sim[movie_index]))

sorted_similar_movie = sorted(similar_movie,key= lambda x:x[1],reverse=True)


for i in range(50):
	print get_title_from_index(sorted_similar_movie[i][0])
    
	

