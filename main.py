from flask import render_template, redirect, url_for, Flask
import pytrends
import pandas as pd
from pytrends.request import TrendReq
from datetime import datetime
from functools import wraps
import time
from collections import Counter

app = Flask(__name__)


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


@timeit
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

@timeit
def count_with_counter_function(str):
    alltext=str.split()
    counter = Counter(alltext)
    return counter


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
    with open('t8shakespeare.txt', 'r') as file:
        data = file.read().replace('\n', '')

    word_count(data)
    count_with_counter_function(data)
    app.run()