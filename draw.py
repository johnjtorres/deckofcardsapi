import requests
import json

url = "https://deckofcardsapi.com/api/deck/new/draw/?count=15"

get_resp = requests.get(url)

get_resp.raise_for_status()

for card in get_resp.json()["cards"]:
    print(card["value"], " of ", card["suit"])