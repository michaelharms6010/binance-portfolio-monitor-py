import schedule
import time
import json
import datetime
import ccxt

keyFile = open(".keys","r")

binanceKey = keyFile.readline().rstrip("\n")
binanceSecret = keyFile.readline().rstrip("\n")
binanceUSKey = keyFile.readline().rstrip("\n")
binanceUSSecret = keyFile.readline().rstrip("\n")


#Binance.us exchange instantiation - uses BINANCE.US keys
exchange_class = getattr(ccxt, "binanceus")
binanceUS = exchange_class({
    "apiKey" : binanceUSKey,
    "secret": binanceUSSecret,
    "timeout": 30000,
    "enableRateLimit": True,
})
print "*** Starting" + binanceUS.id + "Listener ***"

#Connect to Databases
savedDeposits = open("deposit-database.txt", "r")
outDeposits = open("deposit-database.txt", "a")

def job():
    BTCUSD = ( binanceUS.fetch_ticker("BTC/USD")["bid"] + binanceUS.fetch_ticker("BTC/USD")["ask"] ) / 2
    print "BTCUSD Price :" + str(BTCUSD)
    deposits = binanceUS.fetch_deposits()


    for i in deposits:
        savedDeposit = savedDeposits.readline().rstrip("\n")
        # print "Deposit from API:" + str(i)
        # print "Saved Deposit:" + savedDeposit
        
        if str(i) != savedDeposit:
            outDeposits.write(str(i) + "\n")

    
schedule.every(1).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(.1)