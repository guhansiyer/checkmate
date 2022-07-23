import requests
import json

file = open(f"{path}\\Chess Moves.pgn", "r")

read = file.read()

file.close()

response = requests.post("https://lichess.org/api/import",  
    data = {"pgn": read}
)

print(response.json()["url"])
