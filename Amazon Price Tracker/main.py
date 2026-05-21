import lxml
import requests
from bs4 import BeautifulSoup
import smtplib

# get data
url = "the amazon thing link which price you want to track"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ur;q=0.8"
}
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, 'lxml')
# print(soup.prettify())

# Scrap the product title and price
title = soup.find(id="productTitle").get_text().strip()
print(title)
price = soup.find(class_="aok-offscreen").getText()
price_float_without_currency = float(price.split("$")[1])
print(price_float_without_currency)

# Email Alert
BUY_PRICE = 100
if price_float_without_currency < BUY_PRICE:
    message = f"{title} is now {price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("your email, "your app password")
        connection.sendmail(
            from_addr="your email",
            to_addrs="your email",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )