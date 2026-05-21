import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Letting the game load
time.sleep(3)

# Accept website cookies
website_cookies = driver.find_element(By.CSS_SELECTOR, "a.cc_btn.cc_btn_accept_all")
website_cookies.click()

# Selects language
language_select = driver.find_element(By.CSS_SELECTOR, "div#langSelect-EN.langSelectButton.title")
language_select.click()

# Letting the game load again
time.sleep(3)

# Finds THE COOKIE!
almightyCookie = driver.find_element(By.CSS_SELECTOR, "button#bigCookie")

# Begin the nightmare!
while True:
    # The cookie will be clicked for 5 seconds
    time_limit = time.time() + 20
    while time.time() < time_limit:
        almightyCookie.click()

    # Get current cookies count
    currentCookies = driver.find_element(By.ID, "cookies").text.split(" ")
    currentCookies = int(currentCookies[0].replace(',', ''))

    # Search for chepest update you can buy
    try:
        upgrade = driver.find_element(By.CSS_SELECTOR, "div#upgrade0")
    except selenium.common.exceptions.NoSuchElementException:
        pass
    else:
        upgrade.click()

    # Search for strongest auto-clicker you can buy
    options = driver.find_elements(By.CSS_SELECTOR, "div.product")
    selectedProduct = None
    for option in options:
        price = int(option.find_element(By.CSS_SELECTOR, "span.price").text.replace(',', ''))
        if price <= currentCookies:
            selectedProduct = option.get_attribute("id")
            print(selectedProduct)
        else:
            break

    # Handles exception - all products too expensive
    if selectedProduct is None:
        continue
    else:
        driver.find_element(By.ID, selectedProduct).click()