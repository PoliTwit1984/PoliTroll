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
           "Drag queen petting a white siamese cat",
           "Drag queen performing at a festival",
           "Drag queen doing ballet dancing",
           "Drag queen pickoting during a rally",
           "Drag queen sleeping in bed at night with the lamp turned on",
           "Drag queen crying with huge tears running down face",
           "Drag queen driving a Tesla from a distance"
           ]

response = openai.Image.create(
    prompt="jesus wearing makeup",
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']


# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url)  # create HTTP response object

# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("nick.png", 'wb') as f:

    # Saving received content as a png file in
    # binary format

    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)

# username = 'nickbschroer'
# tweets_list = api.user_timeline(
#     screen_name=username, count=1)  # Get the last tweet
# # By default api.user_timeline() gets the last 20 tweets, but you can specify it
# # with the count parameter
# tweet = tweets_list[0]  # An object of class Status (tweepy.models.Status)
# print(tweet.created_at)  # Print the datetime object for the tweet
# print(tweet.text)  # Print the text of the tweet
# print(tweet.in_reply_to_screen_name)
# print(tweet.id)  # Print the username of the user the
# tweet_id = tweet.id
# print(tweet.id)

# media = api.media_upload("drag.png")

# api.update_status(status=".@benbakermo Boo! #dragqeensrule #benbakerisabigot #moleg #benbakerdoesntcareaboutrealissues",
#                   in_reply_to_status_id=tweet_id,  media_ids=[media.media_id])



# # URL of the image to be downloaded is defined as image_url
# r = requests.get(image_url)  # create HTTP response object

# # send a HTTP request to the server and save
# # the HTTP response in a response object called r
# with open("drag.png", 'wb') as f:

#     # Saving received content as a png file in
#     # binary format

#     # write the contents of the response (r.content)
#     # to a new file in binary mode.
#     f.write(r.content)

# username = 'nickbschroer'
# tweets_list = api.user_timeline(
#     screen_name=username, count=1)  # Get the last tweet
# # By default api.user_timeline() gets the last 20 tweets, but you can specify it
# # with the count parameter
# tweet = tweets_list[0]  # An object of class Status (tweepy.models.Status)
# print(tweet.created_at)  # Print the datetime object for the tweet
# print(tweet.text)  # Print the text of the tweet
# print(tweet.in_reply_to_screen_name)
# print(tweet.id)  # Print the username of the user the
# tweet_id = tweet.id
# print(tweet.id)

# media = api.media_upload("nick.png")

# api.update_status(status=".@benbakermo Boo! #dragqeensrule #benbakerisabigot #moleg #benbakerdoesntcareaboutrealissues",
#                   in_reply_to_status_id=tweet_id,  media_ids=[media.media_id])
