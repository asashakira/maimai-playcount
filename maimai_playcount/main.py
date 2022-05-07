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

    play_count = get_play_count(driver)
    print(play_count)

    driver.quit()


if __name__ == "__main__":
    main()
