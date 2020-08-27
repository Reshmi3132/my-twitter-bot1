import tweepy
import os 
def create_api():
  consumer_key = os.getenv('consumer_key')
  consumer_secret = os.getenv('consumer_secret')
  access_token = os.getenv('access_token')
  access_token_secret = os.getenv('access_token_secret')

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print('API Created')
  return api

import time

def follower_count(user):
  emoji_numbers =  {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                      4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}

  uf_split = [int(i) for i in str(user.follower_count)]

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()]) 
  return emoji_followers

api = create_api()

def main():
  while True:
    user = api.get_user('intdummy')
    api.update_profile(name=f'Reshmi|{follower_count(user)} Followers')
    print(f'Updating Twitter Name : Reshmi|{follower_count(user)} Followers')
    print('Waiting to refresh')
    time.sleep(60)
main()

