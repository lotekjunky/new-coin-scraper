import requests

URL = "https://api.kucoin.com/api/v1/market/allTickers"
symbols = set()
usdt = set()
btc = set()
eth = set()
kcs = set()
other = set()


r = requests.get(URL, headers={"Accept": "application/json"})
for symbol in r.json()["data"]["ticker"]:
    symbols.add(symbol["symbol"])

symbols = sorted(symbols)

for asset in symbols:
    tradingpair = asset.split("-")

    if tradingpair[1] == "USDT":
        usdt.add(",KUCOIN:" + tradingpair[0] + tradingpair[1])
    elif tradingpair[1] == "BTC":
        btc.add(",KUCOIN:" + tradingpair[0] + tradingpair[1])
    #elif tradingpair[1] == "ETH":
    #    eth.add(",KUCOIN:" + tradingpair[0] + tradingpair[1])
    #elif tradingpair[1] == "KCS":
    #    kcs.add(",KUCOIN:" + tradingpair[0] + tradingpair[1])
    else:
        other.add(",KUCOIN:" + tradingpair[0] + tradingpair[1])

usdt = sorted(usdt)
btc = sorted(btc)
eth = sorted(eth)
kcs = sorted(kcs)
other = sorted(other)

outputstring = "###USDT"
for each in usdt:
   outputstring = outputstring + each

outputstring = outputstring + ",###BTC"
for each in btc:
    outputstring = outputstring + each

with open("output.txt", "w") as file:
  file.writelines(outputstring)

#
#
# Sample output file should look like this and it should start with 3 consecutive hashmarks
###BTC,KUCOIN:BTCUSDT,KUCOIN:ETHUSDT,###ETH,KUCOIN:QRDOETH,###KCS,KCS:LUNAKCS
#
