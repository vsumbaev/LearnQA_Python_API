import requests
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests
import pytest
import random
import string
import allure

@allure.epic("User register cases")
class TestUserRegister(BaseCase):
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

    @allure.description("This test create user")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("user/",
                                  data=data)
        
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("This test create user with existing email")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("user/",
                                  data=data)
        
        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_content(response, f"Users with email '{email}' already exists")

    @allure.description("This test create user with incorrect email")
    def test_make_user_with_incorrect_email(self):
        self.make_user_data['email'] = 'learnqa'
        response = MyRequests.post("user/",
                                  data=self.make_user_data)
        
        Assertions.assert_response_content(response, "Invalid email format")
        Assertions.assert_code_status(response, 400)

    @allure.description("This test create user with empty fields")
    @pytest.mark.parametrize('make_user_empty_fields', make_user_empty_fields)
    def test_make_user_without_field(self, make_user_empty_fields):
        
        # Get dict data for request from arg 
        make_user_empty_field = next(iter(make_user_empty_fields.values()))
        response = MyRequests.post("user/",
                                 data=make_user_empty_field)
        
        # Get empty value for assert
        make_user_empty_field_by_key = str(''.join(next(iter(make_user_empty_fields.keys()))))

        Assertions.assert_response_content(response, f"The following required params are missed: {make_user_empty_field_by_key}")


    @allure.description("This test create user with short user")
    def test_make_user_with_short_username(self):
        # Generate_random_symbol for request
        random_symbol = ''.join(random.choices(string.ascii_letters + string.digits, k=1))
        self.make_user_data['username'] = random_symbol

        # Make request
        response = MyRequests.post("user/",
                                  data=self.make_user_data)

        Assertions.assert_response_content(response, "The value of 'username' field is too short")
        Assertions.assert_code_status(response, 400)

    @allure.description("This test create user with long user")
    def test_make_user_with_long_username(self):
        # Generate_random_symbol for request
        random_username = ''.join(random.choices(string.ascii_letters + string.digits, k=300))
        self.make_user_data['username'] = random_username

        # Make request
        response = MyRequests.post("user/",
                                  data=self.make_user_data)
        
        Assertions.assert_response_content(response, "The value of 'username' field is too long")
        Assertions.assert_code_status(response, 400)     