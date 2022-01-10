import csv
import json
import pandas as pd

rows = []

csv_read = pd.read_csv("./data/Tweets.csv")

for i in range(0, len(csv_read)):
    message = csv_read["text"][i]
    label = str(" {}".format(csv_read["airline_sentiment"][i]))

    prompt = str("{} ->".format(message))

    rows.append({ "prompt": prompt, "completion": label })

with open('./data/formated.json', 'w') as f:
    json.dump(rows, f, ensure_ascii=True, indent=4)