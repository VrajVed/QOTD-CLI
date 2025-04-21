import requests

response = requests.get("https://zenquotes.io/api/random")
data = response.json()
CYAN  = "\033[33m"
RESET = "\033[0m"

qotd = data[0]['q'] + " - " + data[0]['a']

print(CYAN + qotd + RESET)