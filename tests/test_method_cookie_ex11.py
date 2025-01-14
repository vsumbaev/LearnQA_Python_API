import requests
from lib.my_requests import MyRequests

class TestMethodCookieEx11:
   def test_method_cookie_ex11(self):
    response = MyRequests.get("homework_cookie")
    for i in response.cookies:
       cookie_name = i.name
       print(i.name)
       cookie_value = i.value
       print(i.value)
    assert cookie_name == 'HomeWork' and  cookie_value == 'hw_value'