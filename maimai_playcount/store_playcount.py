""" store playcount """

import csv
from datetime import date


def store_playcount(playcount) -> None:
    today = str(date.today())
    data = [today, playcount]
    with open("playcount.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(data)
