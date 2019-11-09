# to do:
# 1. update asset balance based on withdraws , calculate total portfolio value
# 2. set up listening and displayed alerts for newly detected deposits/withdraws
# 3. STRETCH: enable database for trade tracking


from binance.client import Client
import json
import datetime
import ccxt
import ast

keyFile = open(".keys","r")

binanceKey = keyFile.readline().rstrip("\n")
binanceSecret = keyFile.readline().rstrip("\n")
binanceUSKey = keyFile.readline().rstrip("\n")
binanceUSSecret = keyFile.readline().rstrip("\n")

savedDeposits = []
savedWithdraws = []
accountHoldings = {}

#Connect to database

depositDB = open("deposit-database.txt", "r")
withdrawDB = open('withdraw-database.txt', "r")

#Make a list of deposits

#Compare old list to new deposits (async concerns?)

for i in depositDB:    
    savedDeposits.append(ast.literal_eval(i))

for i in withdrawDB:
    savedWithdraws.append(ast.literal_eval(i))

outDeposits = open("deposit-database.txt", "a")
outWithdraws = open("withdraw-database.txt", "a")

client = Client(binanceKey, binanceSecret)
api = {
    "apiKey": binanceKey,
    "secret": binanceSecret,
    "password": None,
}

newestTrade = client.get_recent_trades(symbol='BTCUSDC')[0]
BTCUSD = float(newestTrade["price"])
print BTCUSD

currentTotalContributionsBTC = 0.0000

for i in savedDeposits:
    if i['token'] in accountHoldings.keys():        
        accountHoldings[i['token']] += i['amount']
    else:
        accountHoldings[i['token']] = i['amount']
        
    currentTotalContributionsBTC += i['depositValueBTC']

currentTotalContributionsUSD = currentTotalContributionsBTC * BTCUSD

print currentTotalContributionsBTC
print currentTotalContributionsUSD

outputObj = {}

print accountHoldings

res = client.get_deposit_history()

for i in res["depositList"]:
    tokenExchangeRateBTC = 1.000
    isNew = True
    for j in savedDeposits:
        if i['txId'] == j['txId']:
            isNew = False
            
            
    if isNew:
        token = i["asset"]
        newDepositAmount = float(i["amount"])
        if token != "BTC":
            tokenExchangeRateBTC = float(client.get_recent_trades(symbol=token +'BTC')[-1]["price"])
        tokenExchangeRateUSD = tokenExchangeRateBTC * BTCUSD
        newTxid = i["txId"]
        newDepositValueBTC = tokenExchangeRateBTC * newDepositAmount
        newDepositValueUSD = newDepositValueBTC * BTCUSD
        depositServerTime = i["insertTime"]
        formattedDepositTime = datetime.datetime.fromtimestamp(depositServerTime/1000)
        depositAddress = i["address"]
        currentTotalContributionsBTC += newDepositValueBTC
        currentTotalContributionsUSD += newDepositValueUSD

        # Print a console alert when a new deposit comes in

        print "\n ***** New deposit detected ***** "
        print "Token Deposited:", token
        print "Amount: ",  newDepositAmount
        print "txid:", newTxid
        print "Servertime of deposit: ",  depositServerTime
        print "Date/Time of deposit: ", formattedDepositTime
        print "Deposited to address: ",  depositAddress
        print "Current Exchange Rate (" + token  + "BTC):",  tokenExchangeRateBTC
        print "Current Exchange Rate (" + token  + "USD):", tokenExchangeRateUSD
        print "Deposit value (BTC): ", newDepositValueBTC
        print "Deposit value (USD): ", newDepositValueUSD
        print "Total portfolio contributions (BTC): ", currentTotalContributionsBTC
        print "Total portfolio contributions (USD): ", currentTotalContributionsUSD
        print "Current portfolio value: "
        print
        outputObj = {
            "token": token,
            "amount": newDepositAmount,
            "txId": newTxid,
            "depositTime": str(formattedDepositTime),
            "depositedTo": depositAddress,
            "exchangeRateBTC": tokenExchangeRateBTC,
            "exchangeRateUSD": tokenExchangeRateUSD,
            "currentTotalContributionsBTC": currentTotalContributionsBTC,
            "currentTotalContributionsUSD": currentTotalContributionsUSD,
            "depositValueBTC": newDepositValueBTC,
            "depositValueUSD": newDepositValueUSD,
            
        }
        #build a db object and write to file
        
        outDeposits.write(str(outputObj)+ "\n")

withdrawRes = client.get_withdraw_history()

for i in withdrawRes["withdrawList"]:
    tokenExchangeRateBTC = 1.000
    isNew = True
    for j in savedWithdraws:
        if i['txId'] == j['txId']:
            isNew = False
            
            
    if isNew:
        token = i["asset"]
        newWithdrawAmount = float(i["amount"])
        if token != "BTC":
            tokenExchangeRateBTC = float(client.get_recent_trades(symbol=token +'BTC')[-1]["price"])
        tokenExchangeRateUSD = tokenExchangeRateBTC * BTCUSD
        newTxid = i["txId"]
        newWithdrawValueBTC = tokenExchangeRateBTC * newWithdrawAmount
        newWithdrawValueUSD = newWithdrawValueBTC * BTCUSD
        withdrawServerTime = i["applyTime"]
        formattedWithdrawTime = datetime.datetime.fromtimestamp(withdrawServerTime/1000)
        withdrawAddress = i["address"]

        # Alert to console

        print "***** New withdrawl detected *****"
        print "Token Withdrawn:", token
        print "Amount: ",  newWithdrawAmount
        print "txid:", newTxid
        print "Servertime of withdraw: ",  withdrawServerTime
        print "Date/Time of withdraw: ", formattedWithdrawTime
        print "Withdrawed to address: ",  withdrawAddress
        print "Current Exchange Rate (" + token  + "BTC):",  tokenExchangeRateBTC
        print "Current Exchange Rate (" + token  + "USD):", tokenExchangeRateUSD
        print "Withdraw value (BTC): ", newWithdrawValueBTC
        print "Withdraw value (USD): ", newWithdrawValueUSD
        print "currentTotalContributions (BTC): ", currentTotalContributionsBTC
        print "currentTotalContributions (USD): ", currentTotalContributionsUSD
        
        
        outputObj = {
            "token": token,
            "amount": newWithdrawAmount,
            "txId": newTxid,
            "withdrawTime": str(formattedWithdrawTime),
            "withdrawnTo": withdrawAddress,
            "exchangeRateBTC": tokenExchangeRateBTC,
            "exchangeRateUSD": tokenExchangeRateUSD,
            "currentTotalContributionsBTC": currentTotalContributionsBTC,
            "currentTotalContributionsUSD": currentTotalContributionsUSD,
            "withdrawValueBTC": newWithdrawValueBTC,
            "withdrawValueUSD": newWithdrawValueUSD,
            
        }
        #build a db object and write to file
        
        outWithdraws.write(str(outputObj)+ "\n")
