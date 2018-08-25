import pandas as pd
import numpy as np
import re,sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

df = pd.read_csv('train.csv', encoding='latin-1')
df = df.drop(['ItemID'],axis=1)
df = df[:10000]

X=np.array(df['SentimentText'])
y=np.array(df['Sentiment'])

cv = CountVectorizer(stop_words='english',strip_accents='ascii',preprocessor=lambda x: re.sub(r'([^a-zA-Z]+)', ' ', x.lower()))
X = cv.fit_transform(X)
X = X.toarray()
X = np.array(X)

#print(cv.get_feature_names())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
mnb = MultinomialNB()
mnb.fit(X_train,y_train)
joblib.dump(mnb,'pickle.pkl')
mnb = joblib.load('pickle.pkl')

#mnb = joblib.load('optimal.pkl')

# userInput = "happy day"
# print(userInput)
# test = cv.transform([userInput])
# test = test.toarray()
# test = np.array(test)


pred = mnb.predict(X_test)
print("Predictions....")
print(pred)
print("The actual output...")
print(y_test)

# pred = mnb.predict(test)
# if pred == 0:
# 	print("Depressed")
# else:
# 	print("Not depressed")

count = 0

for i in range(len(pred)):
	if pred[i] == y_test[i]:
		count = count + 1

print("Number of correct predictions....")
print(count)
print("Out of ...")
print(len(y_test))
print("Accuracy...")
print(str(count/len(y_test)*100)+"%")
