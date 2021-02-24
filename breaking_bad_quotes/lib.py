import requests
def try_me():
    url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
    response = requests.get(url).json()
    print(f"{response[0]['author']}: {response[0]['quote']}")
