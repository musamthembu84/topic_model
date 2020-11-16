import config
import tweepy
import os 
from datetime import datetime
from configparser import ConfigParser
import socket


config_object = ConfigParser()
config_object.read("config.ini")

class TwitterStream(): 
    
    def __init__(self,keys):
        self._ACCESS_TOKEN = None
        self._ACCESS_SECRET = None
        self._CONSUMER_KEY = None
        self._CONSUMER_SECRET = None
        self._keys = config_object["TWITTERAUTH"] 
    
    @property     
    def ACCESS_TOKEN(self):
        return self._keys ["ACCESS_TOKEN"]
    
    @property
    def ACCESS_SECRET(self):
        return self._keys["ACCESS_SECRET"]
    
    @property
    def CONSUMER_KEY(self):
        return self._keys["CONSUMER_KEY"]

    @property
    def CONSUMER_SECRET(self):
        return self._keys["CONSUMER_SECRET"]

def connect_to_twitter_OAuth():
    key = TwitterStream(config_object["TWITTERAUTH"])
    auth = tweepy.OAuthHandler(key.CONSUMER_KEY,key.CONSUMER_SECRET)
    auth.set_access_token(key.ACCESS_TOKEN,key.ACCESS_SECRET)

    api = tweepy.API(auth)
    return api 



def processing_tweets():
    keywords = "#covid19, #coronavirus, #vaccine" 
    api = connect_to_twitter_OAuth()
    covid_date = datetime.today().strftime('%Y-%m-%d')
    language = "en"

    public_tweets = tweepy.Cursor(api.search,
                    q=keywords,
                    lang=language,
                    since=covid_date).items(5)

    for tweet in public_tweets:
        print(tweet.text)



if __name__ == '__main__':
    #processing_tweets()
    new_skt = socket.socket()
    host = "127.0.0.1"
    port = 5555
    new_skt.bind((host,port))
    
    print("Now listening om port: %s" % str(port))

    new_skt.listen(5)
    c, addr = new_skt.accept()

    print("Received request from:" + str(addr))