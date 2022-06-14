""" store playcount """

import json
from datetime import date


def store_play_count(play_count) -> None:
    today = str(date.today())
    new_data = {
        "date": today,
        "playCount": play_count,
    }

    with open("maimai_play_count.json", "r+") as file:
        file_data = json.load(file)
        if file_data["playCounts"][-1]["date"] == today:
            file_data["playCounts"].pop(-1)
        file_data["playCounts"].append(new_data)
        print(file_data)
        #  file.seek(0)
        #  json.dump(file_data, file, indent=2)
