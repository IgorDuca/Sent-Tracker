# Sent-Tracker, AI to detect sentiments from text input

## This AI model is based on GPT-3, by OpenAi.

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Installing](#installing)
- [Response examples](#response_examples)
- [Running](#running)

# About <a name = "about"></a>
### The Sent-Tracker AI was created to help Twitter users to have a better and smoother convivence in the platform, tracking users tweets and then classifying their sentiments, and, if a user had tweeted more then 3 sad tweets, the Sent-Tracker will send to them a couple of help groups, so then that user can talk with someone and feel more connected with other person.

# Getting Started <a name = "getting_started"></a>
### First things first, to use Lawless, you need a [OpenAi](https://beta.openai.com/) API key. If you already have one, just add it to your enviroment variables.
```
export OPENAI_API_KEY="<OPENAI_API_KEY>"
```

# Installing <a name = "installing"></a>
### Install all the libraries that are inside of the ```requirements.txt``` file

```
pip install -r requirements.txt
pip install --upgrade openai
```

# Runing <a name = "running"></a>
### To run the program, you need to run this code snippet in your terminal:
```
python3 bin/main.py
```

### Having any trouble with the installation or while running the program? You can find some help [here](https://beta.openai.com/docs/guides/fine-tuning)