from sklearn.feature_extraction.text import CountVectorizer


text = ["London Paris London","Paris Paris London"]

cv = CountVectorizer()
count_metrix = cv.fit_transform(text)


print count_metrix.toarray()
