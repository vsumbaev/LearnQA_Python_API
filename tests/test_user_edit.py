import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import random
import string


class TestUserEdit(BaseCase, Assertions):
    def test_edit_just_created_user(self):

        # Register
        register_data = self.prepare_registration_data()

        response_register = requests.post("https://playground.learnqa.ru/api/user/",
                                  data=register_data)
        
        Assertions.assert_code_status(response_register, 200)
        Assertions.assert_json_has_key(response_register, "id")

        email = register_data['email']

        #first_name = register_data['firstName']

        #last_name = register_data['lastName']

        password = register_data['password']

        user_id = self.get_json_value(response_register, "id")

        # Login 
        login_data = {

            'email': email,
            'password': password
        }

        response_login = requests.post("https://playground.learnqa.ru/api/user/login",
                                  data=login_data)
        
        auth_sid = self.get_cookie(response_login, "auth_sid")

        token = self.get_header(response_login, "x-csrf-token")


        # Edit
        new_name = "Changed_name"

        response_edit = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}", 
                                     headers={"x-csrf-token":token},
                                     cookies={"auth_sid":auth_sid},
                                     data={"firstName":new_name})
        
        Assertions.assert_code_status(response_edit, 200)

        # Get
        response_get = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
                                    headers={"x-csrf-token":token},
                                    cookies={"auth_sid":auth_sid})
        
        Assertions.assert_json_value_by_name(response_get, "firstName", new_name, "Wrong name of the user after edit")


    def test_edit_no_authorized_user_ex17(self):
        
        # Register
        register_data = self.prepare_registration_data()

        response_register = requests.post("https://playground.learnqa.ru/api/user/",
                                  data=register_data)
        
        Assertions.assert_code_status(response_register, 200)
        Assertions.assert_json_has_key(response_register, "id")

        user_id = self.get_json_value(response_register, "id")

        # Edit
        new_name = "Changed_name"

        response_edit = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
                                     data={"firstName":new_name})
        
        Assertions.assert_code_status(response_edit, 400)
        Assertions.assert_response_content(response_edit, '{"error":"Auth token not supplied"}')

    
    def test_edit_by_another_user_authorized_ex17(self):
        # Register user1
        register_data_user1 = self.prepare_registration_data()

        response_register_user1 = requests.post("https://playground.learnqa.ru/api/user/",
                                  data=register_data_user1)
        
        Assertions.assert_code_status(response_register_user1, 200)
        Assertions.assert_json_has_key(response_register_user1, "id")

        email_user1 = register_data_user1['email']

        password_user1 = register_data_user1['password']

        # Register user2
        register_data_user2 = self.prepare_registration_data()

        response_register_user2 = requests.post("https://playground.learnqa.ru/api/user/",
                                  data=register_data_user2)
                
        Assertions.assert_code_status(response_register_user2, 200)
        Assertions.assert_json_has_key(response_register_user2, "id")

        user_id_user2 = self.get_json_value(response_register_user2, "id")

        # Login 
        login_data = {

            'email': email_user1,
            'password': password_user1
        }

        response_login = requests.post("https://playground.learnqa.ru/api/user/login",
                                  data=login_data)
        
        auth_sid = self.get_cookie(response_login, "auth_sid")

        token = self.get_header(response_login, "x-csrf-token")

        # Edit
        new_name = "Changed_name"

        response_edit = requests.put(f"https://playground.learnqa.ru/api/user/{user_id_user2}", 
                                     headers={"x-csrf-token":token},
                                     cookies={"auth_sid":auth_sid},
                                     data={"firstName":new_name})
        

        Assertions.assert_code_status(response_edit, 400)
        Assertions.assert_response_content(response_edit, '{"error":"This user can only edit their own data."}')


    def test_edit_email_just_created_user_ex17(self):

        # Register
        register_data = self.prepare_registration_data()

        response_register = requests.post("https://playground.learnqa.ru/api/user/",
                                  data=register_data)
        
        Assertions.assert_code_status(response_register, 200)
        Assertions.assert_json_has_key(response_register, "id")

        email = register_data['email']

        #first_name = register_data['firstName']

        #last_name = register_data['lastName']

        password = register_data['password']

        user_id = self.get_json_value(response_register, "id")

        # Login 
        login_data = {

            'email': email,
            'password': password
        }

        response_login = requests.post("https://playground.learnqa.ru/api/user/login",
                                  data=login_data)
        
        auth_sid = self.get_cookie(response_login, "auth_sid")

        token = self.get_header(response_login, "x-csrf-token")


        # Edit
        new_email = "vsumbaev-example.com"

        response_edit = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}", 
                                     headers={"x-csrf-token":token},
                                     cookies={"auth_sid":auth_sid},
                                     data={"email":new_email})
        
        Assertions.assert_code_status(response_edit, 400)
        Assertions.assert_response_content(response_edit, '{"error":"Invalid email format"}')


    def test_edit_short_fisrt_name_just_created_user_ex17(self):

        # Register
        register_data = self.prepare_registration_data()

        response_register = requests.post("https://playground.learnqa.ru/api/user/",
                                  data=register_data)
        
        Assertions.assert_code_status(response_register, 200)
        Assertions.assert_json_has_key(response_register, "id")

        email = register_data['email']

        password = register_data['password']

        user_id = self.get_json_value(response_register, "id")

        # Login 
        login_data = {

            'email': email,
            'password': password
        }

        response_login = requests.post("https://playground.learnqa.ru/api/user/login",
                                  data=login_data)
        
        auth_sid = self.get_cookie(response_login, "auth_sid")

        token = self.get_header(response_login, "x-csrf-token")


        # Edit
        random_symbol_new_name = ''.join(random.choices(string.ascii_letters + string.digits, k=1))

        response_edit = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}", 
                                     headers={"x-csrf-token":token},
                                     cookies={"auth_sid":auth_sid},
                                     data={"firstName":random_symbol_new_name})
        
        Assertions.assert_code_status(response_edit, 400)

        Assertions.assert_response_content(response_edit, '{"error":"The value for field `firstName` is too short"}')