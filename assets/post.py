import requests
import config

file = open(f"{config.path}\\Chess Moves.pgn", "r")

read = file.read()

file.close()

response = requests.post(
    "https://lichess.org/api/import",  
    data = {"pgn": read}
)

url = response.json()["url"]

print(url)