import tweepy, sys
import ddFunction as dd #importing the depression detector

consumer_key = "MuxovZP43J95LeYQPUsnynWkZ" 
consumer_secret = "aRHVauxINpyzr5PXFj5nn8oo2FuKXuRqXpLBUTznucYzNttC9b"
access_key = "348997414-IRu2Je7u3VHLuYbro60oafOuFtf9hwxzbPqKiY13"
access_secret = "0aS7xsI8Hu6XHaxP2wLTJ3BgMxK6rZuCVso0nlq9msuac"
  
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
            print('\n'+j)
            print('\n'+prediction)
            if prediction == 'Suicidal':
                suicidal = True
            elif prediction == 'Possibly suicidal':
                possibly_suicidal += 1.25
            elif prediction == 'Depressed':
                depressed += 1
            else:
                not_depressed += 0.75

        print('\n\nSUMMARY:\n')
        if suicidal == True:
            print('The person is having suicidal thoughts!\n')
        elif possibly_suicidal + depressed < not_depressed:
            print('The person is not depressed\n')
        elif possibly_suicidal > depressed:
            print('The person could be having suicidal thoughts!\n')
        else:
            print('The person is depressed!\n')

if __name__ == '__main__':
    username = sys.argv[1]
    print('\n\n\n')
    get_tweets(username)  