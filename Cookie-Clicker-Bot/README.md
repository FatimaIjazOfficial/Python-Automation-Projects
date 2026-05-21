### Cookie Clicker Bot 

This project demonstrates a bot that automates the clicking and upgrading process for the Cookie Clicker game using Selenium WebDriver. The bot clicks the big cookie continuously and buys upgrades or auto-clickers when affordable.

#### Project Structure
- `cookie_clicker_bot.py`: The main script for the Cookie Clicker bot.

### Usage Instructions

#### Prerequisites
- Install Google Chrome.
- Install `chromedriver` compatible with your version of Chrome. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
- Install the required Python packages:
  ```sh
  pip install selenium
  ```

#### Running the Bot

1. **Clone the repository or download the script**:
   ```sh
   git clone https://github.com/your_username/cookie_clicker_bot.git
   cd cookie_clicker_bot
   ```

2. **Make sure `chromedriver` is in your PATH**:
   - On Windows, place `chromedriver.exe` in the same directory as your script or add its location to the PATH environment variable.
   - On macOS/Linux, place `chromedriver` in `/usr/local/bin` or another directory in your PATH.

3. **Run the script**:
   ```sh
   python cookie_clicker_bot.py
   ```

### Script Overview

1. **Imports**:
   ```python
   import selenium.common.exceptions
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   import time
   ```

2. **Setup**:
   - Configure Chrome options to keep the browser open after the script finishes.
   - Initialize the WebDriver and open the Cookie Clicker game.

   ```python
   chrome_options = webdriver.ChromeOptions()
   chrome_options.add_experimental_option("detach", True)

   driver = webdriver.Chrome(options=chrome_options)
   driver.get("https://orteil.dashnet.org/cookieclicker/")
   ```

3. **Game Initialization**:
   - Wait for the game to load.
   - Accept website cookies and select the English language.

   ```python
   time.sleep(3)
   website_cookies = driver.find_element(By.CSS_SELECTOR, "a.cc_btn.cc_btn_accept_all")
   website_cookies.click()

   language_select = driver.find_element(By.CSS_SELECTOR, "div#langSelect-EN.langSelectButton.title")
   language_select.click()

   time.sleep(3)
   ```

4. **Main Bot Loop**:
   - Locate the big cookie.
   - Continuously click the cookie and attempt to buy upgrades or auto-clickers.

   ```python
   almightyCookie = driver.find_element(By.CSS_SELECTOR, "button#bigCookie")

   while True:
       time_limit = time.time() + 20
       while time.time() < time_limit:
           almightyCookie.click()

       currentCookies = driver.find_element(By.ID, "cookies").text.split(" ")
       currentCookies = int(currentCookies[0].replace(',', ''))

       try:
           upgrade = driver.find_element(By.CSS_SELECTOR, "div#upgrade0")
       except selenium.common.exceptions.NoSuchElementException:
           pass
       else:
           upgrade.click()

       options = driver.find_elements(By.CSS_SELECTOR, "div.product")
       selectedProduct = None
       for option in options:
           price = int(option.find_element(By.CSS_SELECTOR, "span.price").text.replace(',', ''))
           if price <= currentCookies:
               selectedProduct = option.get_attribute("id")
               print(selectedProduct)
           else:
               break

       if selectedProduct is None:
           continue
       else:
           driver.find_element(By.ID, selectedProduct).click()
   ```

### Notes
- Make sure to customize the `url` variable with the correct link for the Cookie Clicker game.
- Ensure `chromedriver` is compatible with your installed version of Chrome.
- Adjust `time.sleep` durations if necessary to ensure the game fully loads before interactions.

### Contributing
Feel free to fork this repository and make improvements or adjustments to the bot. Pull requests are welcome.