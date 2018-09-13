import pandas as pd
import numpy as np
import re,sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib

def depresssion_detect(userInput):
    '''Checking for suicidal tweets'''
    suicidal = False
    suicidalRegEx = ['wan.+d[ie]','end.+(all|it|life)','(kill|hate).+(myself|me)','(took|take).+own.+life','(hang|overdose|poison)','suicid','cut.+hand']

    for s in suicidalRegEx:
        if re.search(s,userInput):
            suicidal = True
            break

    '''Depression detector using ML'''

    df = pd.read_csv('train.csv', encoding='latin-1')
    df = df.drop(['ItemID'],axis=1)
    df = df[:29000]

    X=np.array(df['SentimentText'])
    cv = CountVectorizer(stop_words='english',strip_accents='ascii',preprocessor=lambda x: re.sub(r'([^a-zA-Z]+)', ' ', x.lower()))
    X = cv.fit_transform(X)

    mnb = joblib.load('optimal.pkl') #importing dummped classifier

    test = cv.transform([userInput])
    test = test.toarray()
    test = np.array(test)

    pred = mnb.predict(test)
    if pred == 0 and suicidal == True:
        return 'Suicidal'
    elif pred == 0 and suicidal == False:
        return 'Depressed'
    elif suicidal == True:
        return 'Possibly suicidal'
    else:
        return 'Not depressed'