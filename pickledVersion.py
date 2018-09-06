''' Pickle version of ML for NodeJs server '''

import pandas as pd
import numpy as np
import re,sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib

df = pd.read_csv('train.csv', encoding='latin-1')
df = df.drop(['ItemID'],axis=1)
df = df[:29000]

X=np.array(df['SentimentText'])

cv = CountVectorizer(stop_words='english',strip_accents='ascii',preprocessor=lambda x: re.sub(r'([^a-zA-Z]+)', ' ', x.lower()))
X = cv.fit_transform(X)

mnb = joblib.load('optimal.pkl')

userInput = input('Enter the text to check depression:')
test = cv.transform([userInput])
test = test.toarray()
test = np.array(test)

pred = mnb.predict(test)
if pred == 0:
	print("Depressed")
else:
	print("Not depressed")

sys.stdout.flush()