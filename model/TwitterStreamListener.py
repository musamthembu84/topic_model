import tweepy

ACCESS_TOKEN='703575776936005632-FjYSE9jmQEhl6FGxaLQIp8KGm0N9rEf'
ACCESS_SECRET='VFo08hhyYwJAI8A1QtEDXuZzTCHTkp8hyVNsSZvYFjfYw'
CONSUMER_KEY='ATyQnHGDt5HoWbdC7geil8NgH'
CONSUMER_SECRET='WcjCUT1T554qNuWfp50Kss4pcwY9txrV2hvPBrBuXN0SufzMJj'

def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

    api = tweepy.API(auth)
    return api 

api = connect_to_twitter_OAuth()

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)