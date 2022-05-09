""" gets play history """

from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys


def get_song_name(song_name) -> str:
    song_name = song_name.get_attribute("innerHTML")
    song_name = song_name.split(">")[1]

    return song_name


def get_ac_rate(ac_rate) -> float:
    ac_rate = ac_rate.get_attribute("innerHTML")
    ac_rate = ac_rate.split("<")
    a = ac_rate[0]
    b = ac_rate[1].split(">")[1]
    ac_rate = (a + b).split("%")[0]

    return float(ac_rate)


def get_date(date) -> str:
    date = date.get_attribute("innerHTML")
    return date


def get_play_history(driver) -> list:
    driver.get("https://maimaidx.jp/maimai-mobile/record/")

    song_names = driver.find_elements(By.CLASS_NAME, "break")
    ac_rates = driver.find_elements(By.CLASS_NAME, "playlog_achievement_txt")
    dates = driver.find_elements(
        By.XPATH, "//div[@class='playlog_top_container']/div[1]/span[2]"
    )

    history_size = len(song_names)
    history = []
    for i in range(history_size):
        history.append(
            {
                "name": get_song_name(song_names[i]),
                "ac": get_ac_rate(ac_rates[i]),
                "date": get_date(dates[i]),
            }
        )

    for song in history:
        print(song["name"], song["date"])

    return history
