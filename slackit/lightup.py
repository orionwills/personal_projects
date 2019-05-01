# Posting to a Slack channel
from urllib import request
import json
import sys
import pandas as pd
from datetime import date
import env

COL_DATE = "date"


def send_message_to_slack(
    perp=env.DEFAULT_PERP, fpath="tally.csv", server=env.CODEUP
):
    rlight_icon = ":rotating_light: "
    today = str(date.today())
    df = pd.read_csv(fpath, index_col=COL_DATE)

    # has the perp been lit up before?
    try:
        df.loc[today, perp] += 1
    except KeyError:
        df.loc[today, perp] = 1

    df.to_csv(fpath, index_label=COL_DATE)

    # construct the tally message
    message = f"+1 for {perp}\n\nCurrent Tally\n"

    for col in df.columns:
        nlights = df.loc[today, col]
        message += f"\n{col}: {nlights * rlight_icon} ({nlights})"

    post = {"text": message}

    try:
        json_data = json.dumps(post)
        req = request.Request(
            server,
            data=json_data.encode("ascii"),
            headers={"Content-Type": "application/json"},
        )
        request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))


script_name = sys.argv[0]
args = len(sys.argv)

if args > 1:
    perp = sys.argv[1]
if args > 2:
    fpath = sys.argv[2]
if args > 3:
    server = sys.argv[3]

if args == 2:
    send_message_to_slack(perp)
elif args == 3:
    send_message_to_slack(perp, fpath)
elif args == 4:
    send_message_to_slack(perp, fpath, server)
else:
    print("Wrong number of arguments.")
    print(
        f"Usage: python3 {script_name} [perpetrator] [csv file path] "
        "[server]"
    )
