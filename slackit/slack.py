# Posting emoticons to a Slack channel
from urllib import request, parse
import json
import sys

# Code modified by github.com/orionwills
# Original code from https://www.accadius.com/send-message-slack-python-program/

# Changes made:
# - added count of emoticons to send (argument 1)
# - added which emoticon to send to (argument 2)
# - added server swapper (argumemnt 3)

TEST = 'https://hooks.slack.com/services/your-slack-test-server-here'
ACTUAL = 'https://hooks.slack.com/services/your-slack-actual-server-here'

# defaults
# count defaults to 1
# emoticon defaults to rotating_light
# server defaults to TEST

def send_message_to_slack(count=1, icon='rotating_light', server=TEST):
    
    if server == 'TEST':
        server = 'https://hooks.slack.com/services/your-slack-test-server-here'
    else:
        if server == 'ACTUAL':
            server = 'https://hooks.slack.com/services/your-slack-actual-server-here'

# wraps emoticon with ':'

    message = ":" + icon + ": "
# itirates number of emoticons
    text = message * int(count)

    post = {"text": "{0}".format(text)}
 
    try:
        json_data = json.dumps(post)
        req = request.Request(server,
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))

if len(sys.argv) == 4:
    send_message_to_slack(sys.argv[1], sys.argv[2], sys.argv[3])
elif len(sys.argv) == 3:
    send_message_to_slack(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 2: 
    send_message_to_slack(sys.argv[1])
else:
    print('Something went wrong.')
    sys.exit()