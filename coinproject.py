import re
import requests
from bs4 import BeautifulSoup
from time import time, sleep

url = "https://coinmarketcap.com/currencies/bitcoin/"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")


#the values I need to be presented:
#current worth of 1btc:
curr_worth = soup.find(class_ = "priceValue___11gHJ")
print("The current Price of 1 bitcoin is " + curr_worth.string)

#market cap:
mar_cap = soup.find(class_ = "statsValue___2iaoZ")
print("The market cap of bitcoin " + mar_cap.string)




var = re.search('"(icon-Caret-[up|down]+)"',str(soup)).group(1)



increase = "icon-Caret-up"
decrease = "icon-Caret-down"


#percentage increase/decrease(24hrs)
a = []
for string in soup.find(class_ = "qe1dn9-0 RYkpI"):
    a.append(repr(string))

if(a[0] == '<span class="icon-Caret-down"></span>'):
    a.remove('<span class="icon-Caret-down"></span>')
else:
    a.remove('<span class="icon-Caret-up"></span>')
a.remove("' '")


percent = ''.join(a)
# print(percent)

if(increase == var):
    up = "The current percentage is an increase of " + "+" + percent 
    print(up)
else:
    down = "The current percentage is a decrease of " + "-" + percent
    print(down)


