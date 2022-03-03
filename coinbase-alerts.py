import requests
import json
import time

def post_to_discord(exchange, thing):
    discordUrl = 'https://discord.com/api/webhooks/99999/aaaaa-bbbbb'
    dContent = exchange + " has added " + thing
    data = {"content": dContent}
    response = requests.post(discordUrl, json=data)
    #print(response.status_code)
    return response.status_code


def fetch_json():
    response = requests.request("GET", url, headers=headers)
    return json.loads(str(response.text))


# Variables for the script
url = "https://api.exchange.coinbase.com/products"
headers = {"Accept": "application/json"}

#When starting the script there is no "old" list, so just grab one and use it
USD = []
products = fetch_json()
for asset in products:
    if asset['quote_currency'] == 'USD':
        USD.append(asset['id'])

# The main loop of the script
while True:
    USD_new = []
    for asset in products:
        if asset['quote_currency'] == 'USD':
            USD_new.append(asset['id'])

    # Use this to test adding a new asset
    USD_new.append('BUTT3-USD')

    list_difference = []
    for thing in USD_new:
        if thing not in USD:
            list_difference.append(thing)
            post_to_discord("Coinbase", thing)

    products = ''
    USD = USD_new.copy()
    time.sleep(9)
