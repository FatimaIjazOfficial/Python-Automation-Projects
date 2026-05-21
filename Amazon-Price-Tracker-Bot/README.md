# Amazon Price Tracker Bot Project

## Description

The Amazon Price Tracker Bot is a Python script that monitors the price of a specified product on Amazon. When the price drops below a predefined threshold, the bot sends an email notification to alert you. This tool helps you make timely purchasing decisions based on price changes.

## Prerequisites

Ensure you have the following Python libraries installed:

- `requests`
- `beautifulsoup4`
- `lxml`

You can install them using pip:

```sh
pip install requests beautifulsoup4 lxml
```

## Usage

1. **Fetch Product Data:**
   - The script sends a request to the specified Amazon product page to retrieve its HTML content.
   - It uses BeautifulSoup to parse the HTML and extract the product title and price.

2. **Scrape Product Title and Price:**
   - The script finds the product title using the HTML `id="productTitle"`.
   - It finds the product price using the HTML class `class="aok-offscreen"`.
   - It converts the price to a float value for comparison.

3. **Email Alert:**
   - The script checks if the extracted price is lower than a predefined buy price.
   - If the price is lower, it sends an email alert to notify you of the price drop.

## Steps to Run the Project

1. **Set Up Amazon Product URL:**
   - Replace the placeholder URL in the script with the URL of the Amazon product you want to track:
     ```python
     url = "your_amazon_product_url"
     ```

2. **Configure Email Settings:**
   - Go to the [Google Account Security page](https://myaccount.google.com/security).
   - Under the "Signing in to Google" section, select "App passwords" and generate a new app password for "Mail".
   - Replace the placeholder email and app password in the script with your actual email and generated app password:
     ```python
     result = connection.login("your_email", "your_app_password")
     ```

3. **Set Buy Price:**
   - Set your desired buy price in the script. If the product price drops below this value, you will receive an email alert:
     ```python
     BUY_PRICE = 100  # Replace with your target price
     ```

4. **Run the Script:**
   - Save and run the script. It will fetch the product data, check the price, and send an email alert if the price is below the specified buy price.

## Example Workflow

1. **Fetch Product Data:**
   - The script sends a request to the specified Amazon product URL and parses the HTML content.
   - It extracts the product title and price.

2. **Check Price:**
   - The script checks if the extracted price is lower than the specified buy price.

3. **Send Email Alert:**
   - If the price is lower, the script sends an email alert to notify you of the price drop.

---

#Amazon Price Tracker
This script automates the process of checking the price of an item on Amazon.

**Usage:**
1. Initialize the Chrome WebDriver with options to keep the browser open after the script finishes.
2. Navigate to the desired Amazon product page.
3. Locate the price elements on the page using XPath.
4. Print the price of the product.

## Prerequisites
Ensure you have the following installed on your system:
- Python
- Selenium (`pip install selenium`)
- WebDriver for your browser (e.g., `chromedriver` for Chrome)

## Conclusion
These scripts demonstrate the use of Selenium WebDriver for various web automation tasks. Customize the scripts to fit your specific use cases and ensure that you have the necessary permissions to scrape or automate interactions on the websites you target.

