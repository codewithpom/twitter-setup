import os
import requests
import tweepy

token = os.environ['ACCESS_TOKEN']
token_secret = os.environ['TOKEN_SECRET']
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']


client = tweepy.Client(consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=token,
                       access_token_secret=token_secret)


def get_joke(): 
  url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
  response = requests.get(url)
  hashtags = {
    'python': "#Python",
    'javascript': "#JavaScript",
    "c++": "#CPP",
    "php": "#php",
    'java': "#Java",
    'vue': "#vue",
    'react': "#react",
    ".net": "#csharp",
    "c#": "#csharp"
  }

  default_hashtags = [
    "#programming",
    "#programmingjoke",
    "#programminghumor",
  ]

  extra_langauge_hashtags = [
    "#Python",
    "#javascript",
    "#Java"
  ]

  data = response.json()
  print(response.text, file=open("data.json", 'w'))
  if data['type'] == 'twopart':
    setup = data['setup']
    delivery = data['setup']
    keys = hashtags.keys()
    current_hashtags = []
    for key in keys:
      if key in setup.lower() or key in delivery.lower():
        current_hashtags.append(hashtags[key])

    if len(current_hashtags) == 0:
      current_hashtags = default_hashtags + extra_langauge_hashtags

    return [data, current_hashtags]
  else:
    keys = hashtags.keys()
    current_hashtags = []
    for key in keys:
      if key in data['joke'].lower():
        current_hashtags.append(hashtags[key])

    if len(current_hashtags) == 0:
      current_hashtags = default_hashtags + extra_langauge_hashtags
      
    return [data, current_hashtags]
    

  

def work():
  data = get_joke()
  if data[0]['type'] == "single":
    print("Making tweet")
    print(data[0]['joke'] + "\n\n" + " ".join(data[1]))
    client.create_tweet(text=data[0]['joke'] + "\n\n" + " ".join(data[1]))

  else:
    print('Making double type of tweet')
    tweet = f"{data[0]['setup']}\n\n{data[0]['delivery']}\n" + " ".join(data[1])
    print(tweet)
    client.create_tweet(text=tweet)


def run():
  while True:
    try:
      work()
      break
    except Exception:
      pass

