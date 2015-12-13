#!/bin/bash

# https://api.slack.com/slackbot
slackbot_token=""
# your team prefix on *.slack.com
domain=""
# channel to post message to as slackbot
channel=""

days=$(python -c "from datetime import datetime; print (datetime(2015,12,25)-datetime.now()).days")
{
if [ "$days" -le "0" ]; then
    exit
fi
}
curl --data "Hey @channel, you only have ${days} more days till Christmas"  "https://${domain}.slack.com/services/hooks/slackbot?token=${slackbot_token}&channel=%23${channel}"
