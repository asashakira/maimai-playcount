""" main """

import csv
from datetime import date

from .playcount import get_playcount
from .tweeter import Tweeter

FILE_NAME = "playcount.csv"


def main() -> None:
    tw = Tweeter()

    today = str(date.today())

    with open(FILE_NAME, "r+", encoding="utf-8") as f:
        reader = csv.reader(f)

        l = list(row for row in reader)
        [yesturday, total_playcount_yesturday] = l[-1]

        # don't write if today is written
        if yesturday == today:
            [yesturday, total_playcount_yesturday] = l[-2]
            [today, total_playcount_today] = l[-1]
            playcount = int(total_playcount_today) - int(total_playcount_yesturday)

        else:
            total_playcount = get_playcount()
            data = [today, total_playcount]
            playcount = total_playcount - int(total_playcount_yesturday)

            writer = csv.writer(f)
            writer.writerow(data)

            print(f"Data Written to {FILE_NAME}")

        # print(f"You played {playcount} times on {today}.")
        print(f"{today} の maimai プレイ数: {playcount}")

        response = tw.run(f"{today} の maimai プレイ数: {playcount}")
        print(response)


if __name__ == "__main__":
    main()
