from tweepy import OAuthHandler
from tweepy import Stream #https://docs.tweepy.org/en/v3.9.0/streaming_how_to.html
from tweepy.streaming import StreamListener
from kafka import KafkaProducer
from textblob import TextBlob
import json
import re

#--------Twitter credentials-------------
consumer_key = 'qDP3ASTL1gmqlxqdH91Fxn0ER'
consumer_secret = 'lWmEF44DNvQcpetXrC7AGnqmYNLjnjDqdZpzvdHjP8sVFPvmbT'
access_token = '2308975692-vvaS0lfNd72sNHOiWlpHOaOQQGgIMsvskCbgTpB'
access_token_secret = 'bkVUsfzgDq5I8RxTz0DdY1ZMkst5ofki1u0KnJolM1YGS'

#------------To conncet to Kafka Producer ---------
topic_name = 'Tuwaiq'
kafka_server = 'kafka:9092'

#for more info read  https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html
producer = KafkaProducer(bootstrap_servers=kafka_server, value_serializer=lambda x: json.dumps(x).encode('utf-8'))

#------key word or hashtag to get from stream twitter------
hashtag='data'

#============== Twitter  authentication =============
class TwitterAuth:

    def authenticate(self):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth

#============== Twitter Streamer - main class =============
class TwitterStreamer:

    def __init__(self):
        self.twitterAuth = TwitterAuth()

    def stream_tweets(self):
        while True:
            listener = MyListener()
            auth = self.twitterAuth.authenticate()
            stream = Stream(auth, listener)
            stream.filter(track=[hashtag])

#============== Tweet Listener =============
class MyListener(StreamListener):

    def on_error(self, status_code):
        if status_code == 420:
            return False

    #--------- send tweet to topic-------
    def on_status(self, status):
        if status.retweeted:
            return True
        tweet = self.parse_tweet(status)
        producer.send(topic_name, tweet)
        print(tweet)
        return True
    #--------- parse the tweets-------
    def parse_tweet(self, status):
        text = self.de_emojify(status.text)
        sentiment = TextBlob(text).sentiment # for sentiment analysis

        tweet = {
            "created_at": str(status.created_at),
            "text": text,
            "hashtags": self.extract_hashtags(text),

            "polarity": sentiment.polarity,
            "subjectivity": sentiment.subjectivity,

            "user_id": status.user.id,
            "user_name": status.user.name,

            "user_location": self.de_emojify(status.user.location),
            "user_description": self.de_emojify(status.user.location),

            "user_verified": status.user.verified,
            "user_followers_count": status.user.followers_count,
            "user_statuses_count": status.user.statuses_count,
            "user_created_at": str(status.user.created_at),
            "user_default_profile_image": status.user.default_profile_image,

            "latitude": status.coordinates['coordinates'][0] if status.coordinates else None,
            "longitude": status.coordinates['coordinates'][1] if status.coordinates else None,
        }
        return tweet
    #--------- clean the tweets-------
    @staticmethod
    def clean_tweet(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    #----------remove emoji-------
    @staticmethod
    def de_emojify(text):
        return text.encode('ascii', 'ignore').decode('ascii') if text else None
   #----------extract hashtags-------
    @staticmethod
    def extract_hashtags(text):
        return re.findall(r"#(\w+)", text)


if __name__ == '__main__':
    streamer = TwitterStreamer()
    streamer.stream_tweets()
