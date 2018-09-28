import tweepy, sys
import ddFunction as dd #importing the depression detector

'''Please add consumer_key, consumer_secret, access_key, access_secret from your twitter app here'''
  
def get_tweets(username):

        suicidal = False
        possibly_suicidal = 0
        depressed = 0
        not_depressed = 0

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
        auth.set_access_token(access_key, access_secret) 
        api = tweepy.API(auth)
        tweets = api.user_timeline(screen_name=username)
        tweets_for_csv = [tweet.text for tweet in tweets]  
        for j in tweets_for_csv:
            prediction = dd.depresssion_detect(j)
            print('<br>'+j)
            print('<br><b>'+prediction+'</b><br>')
            if prediction == 'Suicidal':
                suicidal = True
            elif prediction == 'Possibly suicidal':
                possibly_suicidal += 1.25
            elif prediction == 'Depressed':
                depressed += 1
            else:
                not_depressed += 0.75

        print('<br><br><b><i>SUMMARY:</i></b><br>')
        if suicidal == True:
            print('<i>The person is having suicidal thoughts!</i><br>')
        elif possibly_suicidal + depressed < not_depressed:
            print('<i>The person is not depressed</i><br>')
        elif possibly_suicidal > depressed:
            print('<i>The person could be having suicidal thoughts</i><br>')
        else:
            print('<i>The person is depressed!</i><br>')

if __name__ == '__main__':
    username = sys.argv[1]
    get_tweets(username)  