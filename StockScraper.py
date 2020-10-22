# Get S&P ETF price and an email to me when it drops 10% from a predetermined high
# by Kyle Chu, October 22, 2020how t

import requests
import smtplib
import time
from bs4 import BeautifulSoup

#Web Scraping
URL = 'https://finance.yahoo.com/quote/SPY?p=SPY&.tsrc=fin-srch'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'}
page = requests.get(URL, headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')

#Variables
spyTenPercentDrop = 320.4

#Get the name and price from yahoo finance, price is a float
name = soup.find('h1', attrs={"data-reactid": "7"}).text
price = float(soup.find('span', attrs={"data-reactid": "50"}).text)

#Function to check price of ETF
def checking_price():
    if(price < spyTenPercentDrop):
        send_mail()
        return False
    return True

#Function to send mail
def send_mail():
    #Extended mail transer protocol, command sent by an email server to identify itself when connecting to another email server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #Login and Construct Message
    server.login('kylechuf@gmail.com', 'dhvkuhkjfphqquew')
    subject = "Price of " + name + " Dropped"
    body = "Check on Yahoo Finance: https://finance.yahoo.com/quote/SPY?p=SPY&.tsrc=fin-srch"

    #Send Message
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'kylechuf@gmail.com',
        'kwchu255@gmail.com',
        msg
    )
    print("Email Sent")
    server.quit()


#Call Functions
while(checking_price()):
    checking_price()
    time.sleep(10)
print("Out of loop")
