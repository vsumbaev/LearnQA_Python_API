import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests



class TestUserGet(BaseCase):
    def user_auth_by_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1  = MyRequests.post("user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")
        return auth_sid,token,user_id_from_auth_method

    def test_get_user_details_not_auth(self):
        response = MyRequests.get("user/2")
        
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_no_key(response, "email")
        Assertions.assert_json_has_no_key(response, "firstName")
        Assertions.assert_json_has_no_key(response, "lastName")

    
    def test_get_user_details_as_same_user(self):

        auth_sid, token, user_id_from_auth_method = self.user_auth_by_user()

        response = MyRequests.get(f"user/{user_id_from_auth_method}",
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid':auth_sid})
        
        expected_fields = ["username", "email", "firstName", "lastName"]

        Assertions.assert_json_has_keys(response, expected_fields)


    def test_get_user_details_as_another_user(self):

        auth_sid, token, user_id_from_auth_method = self.user_auth_by_user()

        response = MyRequests.get(f"user/1",
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid':auth_sid})
        
        unexpected_fields = ["email", "firstName", "lastName"]

        assert user_id_from_auth_method != 1, f"User id from auth method shouldn't be 1"

        Assertions.assert_json_has_no_keys(response, unexpected_fields)
