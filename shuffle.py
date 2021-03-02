import requests
import json

def shuffle():
    """
    Shuffles the deckofcardsapi deck
    """

    url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

    get_resp = requests.get(url)

    get_resp.raise_for_status()

    print(json.dumps(get_resp.json(), indent=2))

if __name__ == "__main__":
    shuffle()