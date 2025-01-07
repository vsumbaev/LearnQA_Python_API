import requests

class TestMethodCookieEx11:
   def test_method_cookie_ex11(self):
    URL = "https://playground.learnqa.ru/api/homework_cookie"
    response = requests.get(URL)
    for i in response.cookies:
       cookie_name = i.name
       print(i.name)
       cookie_value = i.value
       print(i.value)
    assert cookie_name == 'HomeWork' and  cookie_value == 'hw_value'