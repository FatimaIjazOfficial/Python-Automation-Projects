from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# EXAMPLE
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

# Find the price elements
# price_dollar = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')
# price_cents = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[3]')

# Print the price
print(f"The price is {price_dollar.text} . {price_cents.text}")

driver.quit()