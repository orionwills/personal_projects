## Slack Emoticon Sender

Simple script that uses your channel's slack api to send `x` number of emoticons to said channel.

### Usage
* copy the code or download `slack.py`
* create an env.py file with your slack API URLs and name them `TEST` and `ACTUAL`
* * e.g. TEST = 'https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXX'
* * more info can be [found here](https://api.slack.com/incoming-webhooks)
* run the script with up to three arguments (order matters)
* * number of emoticons to send
* * emoticon text (leave off the colons)
* * which server to send it to (use your test server first)