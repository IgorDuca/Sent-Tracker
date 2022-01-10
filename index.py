import openai
import tweepy
import json
import datetime

auth = tweepy.OAuthHandler("gPQwyhi1viRlEhw61VaKK9t5r", "T8RQEnMactBmzM0GO5JfCc0AICNTrBgdZmUlwuoD575iTU5lSq")
auth.set_access_token("944232963264385026-USagLkOB4gL50Yg9Vv4JUlCdhIOgmag", "PWAbQdIMRU8zyKHsfUPc0uWmY0td1grH6pdPI1GscpUHw")

api = tweepy.API(auth)

openai.api_key = "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"

def getAIResponse(text):
  response = openai.Completion.create(
    model="curie:ft-user-xmlwcnkmjwp9z9z8berwijmz-2021-11-26-01-52-19",
    prompt="{} ->".format(text),
    temperature=0.7,
    max_tokens=1,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  return response

tweets = []
text_emotions = []

pulic_tweets = api.home_timeline(tweet_mode="extended")
for tweet in pulic_tweets:
  tweets.append({ "user": tweet.user.screen_name, "tweet": tweet.full_text, "id": tweet.id_str, "url": "https://twitter.com/{}/status/{}".format(tweet.user.screen_name, tweet.id_str) })

print("Tweet array length: {}".format(len(tweets)))
print("")

positives = []
negatives = []
neutrals = []

for tweet in tweets:
  emotion = getAIResponse(tweet)["choices"][0]["text"].strip()
  text_emotions.append({ "text": tweet, "emotion": emotion })
  
  if(emotion == "positive"): positives.append({ "text": tweet, "emotion": emotion, "url": tweet["url"] })
  if(emotion == "negative"): negatives.append({ "text": tweet, "emotion": emotion, "url": tweet["url"] })
  if(emotion == "neutral"): neutrals.append({ "text": tweet, "emotion": emotion, "url": tweet["url"] })

print(json.dumps(text_emotions))

print("")
print("Text emotions length: {}".format(len(text_emotions)))
print("Comparative: {} -> {}".format(len(tweets), len(text_emotions)))
print("Positive: {} / Neutral: {} / Negative: {}".format(len(positives), len(neutrals), len(negatives)))

print("")

if(len(positives) > 0):
  print(json.dumps(positives))

if(len(negatives) > 0):
  print(json.dumps(negatives))

randomname = "./fetched/{}{}{}.json".format(datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second)

text_emotions.append({ "negative_count": len(negatives), "positive_count": len(positives), "neutral_count": len(neutrals) })

jsonobject = json.dumps(text_emotions, ensure_ascii=True, indent=4)

with open(str(randomname), "w") as outfile:
  outfile.write(jsonobject)
  print("file '{}' wrote".format(randomname))