""" docstring """

import csv
from datetime import date

from .playcount import get_playcount

FILE_NAME = "playcount.csv"


def main() -> None:
    today = str(date.today())

<<<<<<< HEAD
    sega_id = input("SEGA ID: ")
    password = input("PASSWORD: ")
=======
    with open(FILE_NAME, "r+") as f:
        reader = csv.reader(f)
>>>>>>> 173b4bf (refactor)

        l = [row for row in reader]
        [yesturday, total_playcount_yesturday] = l[-1]

        # don't write if today is written
        if yesturday == today:
            [yesturday, total_playcount_yesturday] = l[-2]
            [today, total_playcount_today] = l[-1]
            playcount = int(total_playcount_today) - int(total_playcount_yesturday)
            print(f"You played {playcount} times today.")
            return

        [yesturday, total_playcount_yesturday] = l[-2]
        total_playcount = get_playcount()
        data = [today, total_playcount]
        playcount = total_playcount - int(total_playcount_yesturday)

        writer = csv.writer(f)
        writer.writerow(data)

        print(f"Data Written to {FILE_NAME}")
        print(f"You played {playcount} times today.")


if __name__ == "__main__":
    main()
