from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import keyboard
import time
import threading

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("window-size=1400,1000")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

consent = driver.find_element(By.CSS_SELECTOR, ".fc-button-label")
time.sleep(3)
consent.click()
lang = driver.find_element(By.XPATH, "//*[@id='langSelect-EN']").click()
time.sleep(3)

cookie = driver.find_element(By.ID, "bigCookie")

def check_upgrades():
    threading.Timer(5.0, check_upgrades).start()
    coockies = float(driver.find_element(By.ID, "cookies").text.split()[0].replace(",", "."))

    upgrades = driver.find_elements(By.CSS_SELECTOR, "#upgrades div")
    for upgrade in upgrades:
        upgrade.click()

    items = driver.find_elements(By.CSS_SELECTOR, ".storeSection .price")
    items_list = [float(item.text.replace(",", ".").split(" ")[0]) for item in items if item.text != '']
    print(items_list)
    for buy in items_list[::-1]:
        if buy <= coockies:
            driver.find_element(By.ID, f"product{items_list.index(buy)}").click()


check_upgrades()
on = True
while on:
    cookie.click()
    if keyboard.is_pressed("t"):
        time.sleep(10)
    if keyboard.is_pressed("q"):
        on = False
        driver.quit()
