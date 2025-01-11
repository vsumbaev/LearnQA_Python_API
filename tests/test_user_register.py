import requests
from lib.assertions import Assertions
import pytest
import random
import string


class TestUserRegister:
    make_user_data = {
            'username':'learnqa',
            'password':'password',
            'firstName' : 'learnqa',
            'lastName' : 'learnqa',
            'email' : 'learnqa@email.com'
                }
    make_user_empty_fields = [
            {'username':{'password':'password',
             'firstName' : 'learnqa',
             'lastName' : 'learnqa',
             'email' : 'learnqa@email.com'}},

             {'password':{'username':'learnqa',
             'firstName' : 'learnqa',
             'lastName' : 'learnqa',
             'email' : 'learnqa@email.com'}},
             
             {'firstName':{'username':'learnqa',
             'password':'password',
             'lastName' : 'learnqa',
             'email' : 'learnqa@email.com'}},
             
             {'lastName':{'username':'learnqa',
             'password':'password',
             'firstName' : 'learnqa',
             'email' : 'learnqa@email.com'}},
            
            {'email':{'username':'learnqa',
               'password':'password',
               'firstName' : 'learnqa',
               'lastName' : 'learnqa'}}
                ]
    
    def setup_method(self):
        pass

    def test_make_user_with_incorrect_email(self):
        self.make_user_data['email'] = 'learnqa'
        response = requests.post("https://playground.learnqa.ru/api/user/",
                                  data=self.make_user_data)
        
        Assertions.assert_response_content(response, "Invalid email format")
        Assertions.assert_code_status(response, 400)


    @pytest.mark.parametrize('make_user_empty_fields', make_user_empty_fields)
    def test_make_user_without_field(self, make_user_empty_fields):
        
        # Get dict data for request from arg 
        make_user_empty_field = next(iter(make_user_empty_fields.values()))
        response = requests.post("https://playground.learnqa.ru/api/user/",
                                 data=make_user_empty_field)
        
        # Get empty value for assert
        make_user_empty_field_by_key = str(''.join(next(iter(make_user_empty_fields.keys()))))

        Assertions.assert_response_content(response, f"The following required params are missed: {make_user_empty_field_by_key}")



    def test_make_user_with_short_username(self):
        # Generate_random_symbol for request
        random_symbol = ''.join(random.choices(string.ascii_letters + string.digits, k=1))
        self.make_user_data['username'] = random_symbol

        # Make request
        response = requests.post("https://playground.learnqa.ru/api/user/",
                                  data=self.make_user_data)

        Assertions.assert_response_content(response, "The value of 'username' field is too short")
        Assertions.assert_code_status(response, 400)


    def test_make_user_with_long_username(self):
        # Generate_random_symbol for request
        random_username = ''.join(random.choices(string.ascii_letters + string.digits, k=300))
        self.make_user_data['username'] = random_username

        # Make request
        response = requests.post("https://playground.learnqa.ru/api/user/",
                                  data=self.make_user_data)
        
        Assertions.assert_response_content(response, "The value of 'username' field is too long")
        Assertions.assert_code_status(response, 400)     