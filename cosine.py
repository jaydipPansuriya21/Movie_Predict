from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = ["London Paris London","Paris Paris London"]

cv = CountVectorizer()
count_metrix = cv.fit_transform(text)


#print count_metrix.toarray()
similarity_score = cosine_similarity(count_metrix)

print similarity_score