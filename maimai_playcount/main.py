""" docstring """

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chromedriver_autoinstaller.install()


def get_play_count(sega_id, password, driver) -> int:
    driver.get("https://maimaidx.jp/maimai-mobile/")

    # enter segaid and password
    segaid = driver.find_element(By.NAME, "segaId")
    segaid.send_keys(sega_id)
    password = driver.find_element(By.NAME, "password")
    password.send_keys(password)
    password.send_keys(Keys.RETURN)

    # click aime login
    button = driver.find_element(By.CLASS_NAME, "h_55")
    button.click()

    # jump to player data page
    driver.get("https://maimaidx.jp/maimai-mobile/playerData/")

    # get play count
    element = driver.find_element(By.CLASS_NAME, "f_12")
    plays = element.get_attribute("innerHTML")
    plays = plays.split("：")
    plays = plays[1].split("回")[0]
    plays = plays.split(",")
    plays = "".join(plays)

    print(int(plays))
    return int(plays)


def main() -> None:
    sega_id = input("SEGA ID: ")
    password = input("PASSWORD: ")

    driver = webdriver.Chrome()

    get_play_count(sega_id, password, driver)

    driver.quit()


if __name__ == "__main__":
    main()
