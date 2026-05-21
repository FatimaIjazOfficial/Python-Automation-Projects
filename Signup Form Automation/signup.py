from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME,value="fName")
second_name = driver.find_element(By.NAME,value="lName")
email_address = driver.find_element(By.NAME,value="email")
submit = driver.find_element(By.CSS_SELECTOR, value="form button")

first_name.send_keys("first name")
second_name.send_keys("second name")
email_address.send_keys("your email acount")
submit.click()
