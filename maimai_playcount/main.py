""" docstring """

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#  from .history import get_play_history
from .store_play_count import store_play_count
from .playcount import get_play_count


def main() -> None:
    store_play_count(20)
    return
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
    except:
        print("Login Error")
        return

    play_count = get_play_count(driver)
    #  rating = get_rating(driver)
    #  get_play_history(driver)
    print(play_count)

    driver.quit()


if __name__ == "__main__":
    main()
