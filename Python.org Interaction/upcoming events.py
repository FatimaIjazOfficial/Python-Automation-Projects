from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# print(times)
names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# print(names)
events = {}

for n in range(len(times)):
    events[n] = {
        "time": times[n].text,
        "name": names[n].text,
    }
print(events)
driver.quit()