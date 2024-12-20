import requests
method = "https://playground.learnqa.ru/api/long_redirect"
response = requests.get(method, allow_redirects=True)
print(len(response.history))
print(response.url)