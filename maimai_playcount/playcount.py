""" gets play count """

from selenium.webdriver.common.by import By


def get_playcount(driver) -> int:
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
