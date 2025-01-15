from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure
import time

@allure.epic("Deletion cases")
class TestUserDelete(BaseCase, MyRequests):

    @allure.description("This test delete user with id 2")
    @allure.title("Проверка удаления юзера c id 2")
    @allure.id("1")
    @allure.label("component", "API tests")
    @allure.issue("Ex18: Тесты на DELETE")
    def test_user_id_2_delete_ex18(self):
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
            }

        response_login = MyRequests.post("user/login", data=login_data)

        Assertions.assert_code_status(response_login, 200)


        auth_sid = self.get_cookie(response_login, "auth_sid")

        token = self.get_header(response_login, "x-csrf-token")


        response_delete = MyRequests.delete(url="user/2", headers={"x-csrf-token":token}, cookies={"auth_sid":auth_sid})

        Assertions.assert_code_status(response_delete, 400)
        Assertions.assert_response_content(response_delete, '{"error":"Please, do not delete test users with ID 1, 2, 3, 4 or 5."}')
    
    @allure.description("This test successfully deletes the created user.")
    @allure.title("Проверка удаления юзера")
    @allure.id("2")
    @allure.label("component", "API tests")
    @allure.issue("Ex18: Тесты на DELETE")
    def test_user_delete_ex18(self):
        # Register
        register_data = self.prepare_registration_data()

        response_register = MyRequests.post("user/", data=register_data)
        
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

        response_login = MyRequests.post("user/login", data=login_data)

        Assertions.assert_code_status(response_login, 200)

        auth_sid = self.get_cookie(response_login, "auth_sid")

        token = self.get_header(response_login, "x-csrf-token")

        
        # Delete
        response_delete = MyRequests.delete(url=f"user/{user_id}", headers={"x-csrf-token":token}, cookies={"auth_sid":auth_sid})

        Assertions.assert_code_status(response_delete, 200)


        # Get removed user by id 
        response_get_id = MyRequests.get(f"user/{user_id}")

        Assertions.assert_code_status(response_get_id, 404)

        Assertions.assert_response_content(response_get_id, 'User not found')


    @allure.description("This test try to delete created user2 by user1.")
    @allure.title("Проверка удаления юзера дргуим юзером")
    @allure.id("3")
    @allure.label("component", "API tests")
    @allure.issue("Ex18: Тесты на DELETE")
    def test_user_delete_another_user_ex18(self):
        # Register user1
        register_data_user1 = self.prepare_registration_data()

        response_register_user1 = MyRequests.post("user/", data=register_data_user1)
        
        Assertions.assert_code_status(response_register_user1, 200)
        Assertions.assert_json_has_key(response_register_user1, "id")

        email_user1 = register_data_user1['email']

        password_user1 = register_data_user1['password']


        # Register user 2
        register_data_user2 = self.prepare_registration_data()

        time.sleep(5)

        response_register_user2 = MyRequests.post("user/", data=register_data_user2)
        
        Assertions.assert_code_status(response_register_user2, 200)
        Assertions.assert_json_has_key(response_register_user2, "id")

        user_id_user2 = self.get_json_value(response_register_user2, "id")

        # Login user 1
        login_data_user1 = {

            'email': email_user1,
            'password': password_user1
        }

        response_login_user1 = MyRequests.post("user/login", data=login_data_user1)

        Assertions.assert_code_status(response_login_user1, 200)

        auth_sid_user1 = self.get_cookie(response_login_user1, "auth_sid")

        token_user1 = self.get_header(response_login_user1, "x-csrf-token")

        # Delete user 2
        response_delete_user2 = MyRequests.delete(url=f"user/{user_id_user2}", headers={"x-csrf-token":token_user1}, cookies={"auth_sid":auth_sid_user1})

        Assertions.assert_code_status(response_delete_user2, 400)
        Assertions.assert_response_content(response_delete_user2, '{"error":"This user can only delete their own account."}')

