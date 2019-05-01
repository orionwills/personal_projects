# Posting to a Slack channel
from urllib import request
import json
import sys
import pandas as pd
from datetime import date
import env

COL_DATE = "date"


def send_message_to_slack(
    perp=env.DEFAULT_PERP, fpath="tally.csv", server=env.DEFAULT_SERVER
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
    message = f"+1 for {perp}\n\n"
    message += "Current Tally\n"
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

if 2 <= args <= 4:
    send_message_to_slack(*sys.argv[1:args])
else:
    print("Wrong number of arguments.")
    print(
        f"Usage: python3 {script_name} [perpetrator] [csv file path] "
        "[server]"
    )
