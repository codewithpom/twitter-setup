import os
import tweepy
import time
import random
import json


token = os.environ['ACCESS_TOKEN']
token_secret = os.environ['TOKEN_SECRET']
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)


client = tweepy.Client(consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=token,
                       access_token_secret=token_secret)


def get_joke(): 
    file = open("data.json")
    data = json.loads(file.read())
    file.close()
    joke = random.choice(data['programming_jokes'])
    others = "#programming #programmingjoke #programminghumor #Python #Javascript".split(" ")
    for o in others:
      joke['hashtags'].append(o)
      
    return [joke['joke'], joke['hashtags']]
    

  

def work():
  data = get_joke()
  
  print("Making tweet")
  print(data[0] + "\n\n" + " ".join(data[1]))
  data = client.create_tweet(text=data[0] + "\n\n" + " ".join(data[1]))
  return data

def run():  
  data = work()
  id = data.data['id']
  
    
    


run()
