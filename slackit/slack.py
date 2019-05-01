# Posting to a Slack channel
from urllib import request, parse
import json
import sys
from env import TEST, ACTUAL

def send_message_to_slack(count, icon='rotating_light', server=ACTUAL):
    
    if server == 'ACTUAL':
        server = ACTUAL
    else:
        server = TEST

    message = ":" + icon + ": "
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