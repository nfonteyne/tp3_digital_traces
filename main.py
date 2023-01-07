from flask import render_template, redirect, url_for, Flask
import pytrends
import pandas as pd
from pytrends.request import TrendReq
from datetime import datetime

# execute the TrendReq method by passing the host language (hl) and timezone (tz) parameters


app = Flask(__name__)


@app.route("/")
def trend():

    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(kw_list=['switch','ps5'])
    interest_over_time_df = pytrends.interest_over_time()
    switch = interest_over_time_df['switch'].values.tolist()
    ps5 = interest_over_time_df['ps5'].values.tolist()
    dates = [datetime.fromtimestamp(int(date/1e9)).date().isoformat() for date in interest_over_time_df.index.values.tolist()]

    return render_template('main.html', labels=dates, myswitch=switch, myps5=ps5)

if __name__ == "__main__":
    app.run()