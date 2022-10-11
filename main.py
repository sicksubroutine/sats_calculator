import requests
import time

exit = False
def btc_price_get():
  global price
  key = "https://api.kraken.com/0/public/Ticker?pair=xbtusd"
  r = requests.get(key)
  data = r.json()["result"]["XXBTZUSD"]["c"]
  price = round(float(data[0]))
  return price
def main():
  global exit, price
  sats = 0.00000001
  full_btc = 100000000
  btc_price_get()
  print("\33[34m=== Convert between sats and USD! ===\33[0m")
  print("Current BTC Price on Kraken: \33[32m$"+ str(price) + "\33[0m")
  choice = input("\33[35m=== What would you like to do? ===\33[0m \n1. Input USD to get amount of sats. \n2. Input Sats to get an amount of USD. \n3. Exit\n> ")
  if choice == "1":
    print("How much USD would you like to input?")
    USD = float(input("$"))
    amount_btc = (USD / price) / sats
    print("$" + str(USD) + " equals " + "\33[31m"+str(round(amount_btc)) + " sats\33[0m!")
    a = float(round(amount_btc / full_btc, 8))
    print("Or \33[32m" + str('{:.8f}'.format(a)) + "\33[0m in full BTC terms!")
  elif choice == "2":
    what_amount = int(input("How many sats? "))
    answer = what_amount * sats
    answer2 = round(answer * price + 0.006, 2)
    print(str(what_amount) + " sats")
    print(str("\33[32m" + '{:.8f}'.format(answer)) + " BTC\33[0m")
    print("\33[31m$" + str(answer2) + " worth of sats\33[0m/BTC.")
    return main()
  elif choice == "3":
    print("I'm sorry you feel that way! Terminating interface. ")
    print("...")
    time.sleep(1)
    exit = True
    return
  else:
    print("\33[31mInvalid choice.\33[0m")
    time.sleep(1)
    return main()
while exit == False:
  main()