import random

import openai
import requests
import tweepy

import config

openai.api_key = config.openai_key

client = tweepy.Client(config.bearer_token,
                       config.consumer_key,
                       config.consumer_secret,
                       config.access_token,
                       config.access_token_secret)


auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)

auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

ai_list = ["Drag Queen looking at a man on a park bench",
           "Drag queen dancing in the rain",
           "Drag queen playing with a puppy in a field",
           "Drag queen sitting on the Capitol steps",
           "Drag queen petting a dachshund",
           "Drag queen performing at a festival",
           "Drag queen doing ballet dancing",
           "Drag queen pickoting during a rally",
           "Drag queen sleeping in bed at night with the lamp turned on",
           "Drag queen crying with huge tears running down face",
           "Drag queen driving a Tesla from a distance"
           "Drag queen twerking in front of an audience"
           ]

nickbschroer_id = "4591016128"
tweet_text = "@nickbschroer is a bigot! #moleg"
#tweet_text = "Ben, care about real issues, please?!?!"

response = client.get_users_tweets(id=nickbschroer_id, max_results=5)

nickbschroer_last_tweet_id = response.data[0].id
nickbschroer_last_tweet_text = response.data[0].text

print(nickbschroer_last_tweet_id)
print(nickbschroer_last_tweet_text)

if not nickbschroer_last_tweet_text.startswith("RT"):

    ai_text = (random.choice(ai_list))

    responseai = openai.Image.create(
    prompt=ai_text,
    n=1,
    size="1024x1024")

    image_url = responseai['data'][0]['url']
    r = requests.get(image_url)

    with open("drag.png", 'wb') as f:
        f.write(r.content)

    media = api.media_upload("drag.png")  

    client.create_tweet(text=tweet_text, in_reply_to_tweet_id=nickbschroer_last_tweet_id, media_ids=[media.media_id])
    print("Tweeted!")
else:
    print("Last tweet was RT")