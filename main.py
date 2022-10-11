import requests
import json
import time

exit = False
def init():
  global exit, data, price, sats
  exit = False
  key = "https://api.kraken.com/0/public/Ticker?pair=xbtusd"
  r = requests.get(key)
  data = r.json()
  data = r.json()["result"]["XXBTZUSD"]["c"]
  data = data[0]
  price = float(data)
  price = int(round(price))
  sats = 0.00000001
def main():
  global exit, data, sats, price
  full_btc = 100000000
  choice = input("What would you like to do?\n1. Input USD to get amount of sats. \n2. Input Sats to get an amount of USD. \n3. Exit\n")
  if choice == "1":
    print("How much USD would you like to input?")
    USD = input("$")
    USD = float(USD)
    price = float(price)
    amount_btc = USD / price
    amount_btc = amount_btc / sats
    USD = int(USD)
    print("$" + str(USD) + " equals " + "\33[31m"+str(round(amount_btc)) + " sats\33[0m!")
    if amount_btc > 10000:
      a = amount_btc / full_btc
      a = float(a)
      a = round(a, 8)
      print("Or \33[32m" + str(a) + "\33[0m in full BTC terms!")
  elif choice == "2":
    what_amount = input("How many sats? ")
    what_amount = int(what_amount)
    answer = what_amount * sats
    answer2 = answer * price
    answer2 = answer2 + 0.006
    answer2 = round(answer2, 2)
    print(str(what_amount) + " sats")
    print(str(round(answer,8)) + " BTC")
    
    print("\33[31m$" + str(answer2) + " worth of sats\33[0m/BTC.")
    return main()
  elif choice == "3":
    exit = True
    return
  else:
    print("\33[31mInvalid choice.\33[0m")
    time.sleep(1)
    return main()
while exit == False:
  init()
  main()