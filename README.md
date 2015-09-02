# Slackbot-Send
Simple command line utility for easily sending messages to Slack via Slackbot

## Config
Before using it, you need to set your slack domain and the slackbot token in `config.json`.
You can get a token from https://my.slack.com/services/new/slackbot

## Usage

    python3 main.py <channel> <message>

Example (will send "Hello from Slackbot." to #general):

    python3 main.py general Hello from Slackbot.

**The channel parameter should not contain the hashtag '#'.**