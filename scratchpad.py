#Binance.us exchange instantiation - uses BINANCE.US keys
# exchange_class = getattr(ccxt, "binanceus")
# binanceUS = exchange_class({
#     "apiKey" : binanceUSKey,
#     "secret": binanceUSSecret,
#     "timeout": 30000,
#     "enableRateLimit": True,
# })
# #print "*** Starting " + binanceUS.id + " Listener ***"
# #Calculates arithmetic mean of bid and ask prices

# BTCUSD = ( binanceUS.fetch_ticker("BTC/USD")["bid"] + binanceUS.fetch_ticker("BTC/USD")["ask"] ) / 2

# print str(zecData)
# token = res["depositList"][-1]["asset"]

# newDepositAmount = float(res["depositList"][-1]["amount"])
# tokenExchangeRateBTC = float(client.get_recent_trades(symbol=token +'BTC')[-1]["price"])
# tokenExchangeRateUSD = tokenExchangeRateBTC * BTCUSD
# newTxid = res["depositList"][-1]["txId"]
# newDepositValueBTC = tokenExchangeRateBTC * newDepositAmount
# newDepositValueUSD = newDepositValueBTC * BTCUSD
# depositServerTime = res["depositList"][-1]["insertTime"]
# formattedDepositTime = datetime.datetime.fromtimestamp(depositServerTime/1000)
# depositAddress = res["depositList"][-1]["address"]

# print "Token Deposited:", token
# print "Amount: ",  newDepositAmount
# print "txid:", newTxid
# print "Servertime of deposit: ",  depositServerTime
# print "Date/Time of deposit: ", formattedDepositTime
# print "Deposited to address: ",  depositAddress
# print "Current Exchange Rate (" + token  + "BTC):",  tokenExchangeRateBTC
# print "Current Exchange Rate (" + token  + "USD):", tokenExchangeRateUSD
# print "Deposit value (BTC): ", newDepositValueBTC
# print "Deposit value (USD): ", newDepositValueUSD

# #This info relies on db design
# print "Total BTC Value Contributed: "
# print "Total USD Value Contributed: "
# print "Current Portfolio Value: "

# outputObj = {
#     "token": token,
#     "amount": newDepositAmount,
#     "txId": newTxid,
#     "depositTime": str(formattedDepositTime),
#     "depositedTo": depositAddress,
#     "exchangeRateBTC": tokenExchangeRateBTC,
#     "exchangeRateUSD": tokenExchangeRateUSD,
#     "currentTotalContributionsBTC": 0,
#     "currentTotalContributionsUSD": 0
# }