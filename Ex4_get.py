import requests

URI = "https://playground.learnqa.ru/api/get_text"

print(requests.get("https://playground.learnqa.ru/api/get_text").text)