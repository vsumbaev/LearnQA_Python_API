import requests
import json

class TestMethodHeadersEx12:

    def test_method_headers_ex12(self):
        URL = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(URL)
        headers = str(response.headers)
        headers = headers.replace("\'", "\"")
        assert json.loads(headers)['x-secret-homework-header'] == "Some secret value"
            