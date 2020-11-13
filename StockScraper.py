# Get chosen stock price and send an email to user when it drops a chosen percent from a conservative 52 week high
# By Kyle Chu, Started October 22, 2020

import requests
import smtplib
import time
from bs4 import BeautifulSoup

#Get Input from User:
print("I will email you when a stock drops a certain percent below its peak (3 percent below 52 week range to be conservative)")
symbol = input("Enter Stock Symbol: ").upper()
desiredPercentDrop = float(input("Enter Desired Percent Drop (ex. 10, 15, 20): "))
conservativePeak = .97
finalDesiredPercentOf = (100 - desiredPercentDrop)/100

#Web Scraping
URL = 'https://finance.yahoo.com/quote/'+ symbol +'?p='+ symbol +'&.tsrc=fin-srch'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'}
page = requests.get(URL, headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')

#Get the name and price from yahoo finance, price is a float
name = soup.find('h1', attrs={"data-reactid": "7"}).text
currentPrice = float(soup.find('span', attrs={"data-reactid": "50"}).text)
getPeakPrice = soup.find('td', attrs={"data-reactid": "121"}).text

#Get the target price to either email or not email
peakPriceWithDrop = (float(getPeakPrice.split('-')[1].strip()) * conservativePeak) * finalDesiredPercentOf

#Function to check price of ETF
def checking_price():
    if(currentPrice < peakPriceWithDrop):
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
    body = "Check on Yahoo Finance: " + URL

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
print("looping started")
while(checking_price()):
    checking_price()
    time.sleep(10)
print("Out of loop")
