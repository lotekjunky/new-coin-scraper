# new-coin-scraper
This will be a collection of scripts which use APIs to scrape crypto currency exchanges for trading pair data. As I have time to work on this, I'll add more exchanges and more features.
<hr>
<b>Currently working:</b>
<br>
<i>kucoin.py</i>
<br>
Uses the public market API from kucoin.com to sort and group all assets by trading pair. It then pieces those sets together into output.txt which is suitable for importing into tradingview.com
<br><br>
<b>Published but not finished or really working yet:</b>
<br>
<i>coinbase-alerts.py</i>
<br>
Uses the public market API from coinbase.com to gather all tradeable assets and stores them memory resident.
It then sleeps X minutes and does it again, comparing the two lists. 
It's supposed to be able to send an alert to a discord channel when a new asset is found. it works in debug, but it doesn't actually fire off. Still need to do some debugging I guess.
