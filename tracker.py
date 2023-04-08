import requests
from bs4 import BeautifulSoup
import smtplib #gotta use this to send email alerts

#set a buy price!
BUY_PRICE = 100
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
#this is the metadata we need to send to amazon so that this program won't be detected as a bot 
USER_AGENT = "METADATA" #get your user_agent here: https://www.whatismybrowser.com/detect/what-is-my-user-agent/
gpw_amazon_url = 'https://www.amazon.com/Logitech-Wireless-Gaming-Esports-Performance/dp/B07GCKQD77/ref=sr_1_7_sspa?keywords=darmoshark&qid=1678335617&sprefix=darmo%2Caps%2C165&sr=8-7-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFaTk5LMUZBMUI3NEsmZW5jcnlwdGVkSWQ9QTAwNjQwMzczR0hEQURYSVlMOEhYJmVuY3J5cHRlZEFkSWQ9QTEwMDczOTYzNEQwNVJEWUVPUklFJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

# this is the product I am trying to get below 100, you can easily modify it to check multiple items in one run
request = requests.get("https://www.amazon.com/Logitech-Wireless-Gaming-Esports-Performance/dp/B07GCKQD77/ref=sr_1_7_sspa?keywords=darmoshark&qid=1678335617&sprefix=darmo%2Caps%2C165&sr=8-7-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFaTk5LMUZBMUI3NEsmZW5jcnlwdGVkSWQ9QTAwNjQwMzczR0hEQURYSVlMOEhYJmVuY3J5cHRlZEFkSWQ9QTEwMDczOTYzNEQwNVJEWUVPUklFJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==", headers = {"User-Agent": USER_AGENT, "Accept-Language": ACCEPT_LANGUAGE})

#using beatiful soup again
soup = BeautifulSoup(request.text, "lxml")#use lxml parser instead of html

title = soup.find(id="productTitle").get_text().strip()#gets the name of the product

price_whole = soup.find("span", class_ = "a-price-whole").getText() #gets hold of the price before the decimal
price_fraction = soup.find("span", class_ = "a-price-fraction").getText() #after the decimal


total_price = float(price_whole + price_fraction)

if total_price <= BUY_PRICE:
    message = f"{title} is now ready to purchase with the price being at {total_price}.\nURL: {gpw_amazon_url}"

    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        result = connection.login("1234ggg@gmail.com", "youshallnotpass")#here, you gotta pass in an email address and it's corresponding password
        connection.sendmail(
            from_addr = "1234ggg@gmail.com", 
            to_addrs = "1234ggg@gmail.com", 
            msg = f"Subject:Amazon Price Alert!\n\n{message}")