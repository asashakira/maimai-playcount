""" gets play count """

import sys

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_playcount(sega_id: str, sega_password: str) -> int:
    chromedriver_autoinstaller.install()

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://maimaidx.jp/maimai-mobile/")

    # login
    try:
        # enter segaid
        e = driver.find_element(By.NAME, "segaId")
        e.send_keys(sega_id)
        # enter password
        e = driver.find_element(By.NAME, "password")
        e.send_keys(sega_password)
        # press enter
        e.send_keys(Keys.RETURN)
        # click aime login
        button = driver.find_element(By.CLASS_NAME, "h_55")
        button.click()
    except NoSuchElementException:
        print("LOGIN ERROR")
        print("Did you set SEGA_ID and SEGA_PASSWORD environment variable?")
        sys.exit(1)

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
