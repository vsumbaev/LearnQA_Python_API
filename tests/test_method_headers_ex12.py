import requests
import json
from lib.my_requests import MyRequests


class TestMethodHeadersEx12:

    def test_method_headers_ex12(self):
        response = MyRequests.get("homework_header")
        headers = str(response.headers)
        headers = headers.replace("\'", "\"")
        assert json.loads(headers)['x-secret-homework-header'] == "Some secret value"
            