""" main """

import csv
from datetime import date, timedelta
import sys

from .playcount import get_playcount
from .tweeter import Tweeter

FILE_NAME = "playcount.csv"


def main() -> None:
    args = sys.argv[1:]

    if len(args) < 2:
        print("Usage: playcount <SEGA_ID> <PASSWORD>")
        return

    sega_id = args[0]
    password = args[1]

    tw = Tweeter()

    # technically not today since it's 1AM...
    today = str(date.today() - timedelta(1))

    with open(FILE_NAME, "r+", encoding="utf-8") as f:
        reader = csv.reader(f)

        l = list(row for row in reader)
        [yesterday, total_playcount_yesterday] = l[-1]

        # don't write if today is written
        if yesterday == today:
            [yesterday, total_playcount_yesterday] = l[-2]
            [today, total_playcount_today] = l[-1]
            playcount = int(total_playcount_today) - int(total_playcount_yesterday)

        else:
            total_playcount = get_playcount(sega_id, password)
            data = [today, total_playcount]
            playcount = total_playcount - int(total_playcount_yesterday)

            writer = csv.writer(f)
            writer.writerow(data)

            print(f"Data Written to {FILE_NAME}")

        # print(f"You played {playcount} times on {today}.")
        print(f"{today} の maimai プレイ数: {playcount}")

        # if playcount > 0:
            # response = tw.run(f"{today} の maimai プレイ数: {playcount}")
            # print(response)


if __name__ == "__main__":
    main()
