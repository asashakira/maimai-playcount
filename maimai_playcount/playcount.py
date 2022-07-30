""" gets play count """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import chromedriver_autoinstaller


def get_playcount() -> int:
    chromedriver_autoinstaller.install()

    # sega_id = input("SEGA ID: ")
    # password = input("PASSWORD: ")
    sega_id = "asakira"
    password = "pikmin0340"

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
    except NoSuchElementException as e:
        print(e)
        return -1

    # jump to player data page
    driver.get("https://maimaidx.jp/maimai-mobile/playerData/")

    # get play count
    e = driver.find_element(By.CLASS_NAME, "f_12")
    plays = e.get_attribute("innerHTML")
    plays = plays.split("：")
    plays = plays[1].split("回")[0]
    plays = plays.split(",")
    plays = "".join(plays)

    driver.quit()

    return int(plays)
