""" docstring """

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_play_count(driver) -> int:
    # jump to player data page
    driver.get("https://maimaidx.jp/maimai-mobile/playerData/")

    # get play count
    e = driver.find_element(By.CLASS_NAME, "f_12")
    plays = e.get_attribute("innerHTML")
    plays = plays.split("：")
    plays = plays[1].split("回")[0]
    plays = plays.split(",")
    plays = "".join(plays)

    return int(plays)


def get_rating(driver) -> int:
    # jump to player data page
    driver.get("https://maimaidx.jp/maimai-mobile/playerData/")

    # get rating
    e = driver.find_element(By.CLASS_NAME, "rating_block")
    rating = e.get_attribute("innerHTML")

    return int(rating)


def get_play_history(driver) -> list:
    driver.get("https://maimaidx.jp/maimai-mobile/record/")
    song_names = driver.find_elements(By.CLASS_NAME, "break")
    ac_rates = driver.find_elements(By.CLASS_NAME, "playlog_achievement_txt")

    history_size = len(song_names)
    history = []
    for i in range(history_size):
        song_name = song_names[i].get_attribute("innerHTML")
        song_name = song_name.split(">")[1]
        ac_rate = ac_rates[i].get_attribute("innerHTML")
        ac_rate = ac_rate.split("<")
        a = ac_rate[0]
        b = ac_rate[1].split(">")[1]
        ac_rate = (a + b).split("%")[0]
        history.append(
            {
                "name": song_name,
                "ac": ac_rate,
            }
        )

    for song in history:
        print(song["name"], song["ac"])

    return history


def main() -> None:
    chromedriver_autoinstaller.install()

    sega_id = input("SEGA ID: ")
    password = input("PASSWORD: ")

    driver = webdriver.Chrome()
    driver.get("https://maimaidx.jp/maimai-mobile/")

    # login
    try:
        # enter segaid
        e = driver.find_element(By.NAME, "segaId")
        e.send_keys(sega_id)
        # enter password
        e = driver.find_element(By.NAME, "password")
        e.send_keys(password)
        # press enter
        e.send_keys(Keys.RETURN)
        # click aime login
        button = driver.find_element(By.CLASS_NAME, "h_55")
        button.click()
    except:
        print("Login Error")
        return

    # play_count = get_play_count(driver)
    # rating = get_rating(driver)
    get_play_history(driver)

    driver.quit()


if __name__ == "__main__":
    main()
