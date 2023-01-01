'''
A quick script to fetch the id of a channel you want to use.

USAGE: python fetchChannelId.py <channel_name>
'''

import requests
import sys
import os
import json
from dotenv import load_dotenv


load_dotenv()

# Environment variables must be set with your tokens
BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')

HASH = "%23"

channelName = sys.argv[1]

params = {"token": BOT_TOKEN}

# Capture Response as JSON
response = requests.get("https://slack.com/api/channels.list", params=params)
channels = json.loads(response.text)["channels"]

for channel in channels:
  if channel["name"] == channelName:
    print channel["id"]
    break
