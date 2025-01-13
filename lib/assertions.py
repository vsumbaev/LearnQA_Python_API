import json
from requests import Response

class Assertions:
    staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"

        assert name in response_as_dict, f"Response JSON doesn't have key {name}"
        assert response_as_dict[name] == expected_value, error_message

    staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, f"Unexpected status code. Status code is {response.status_code}. Expected status code is {expected_status_code}" 
    
    staticmethod
    def assert_response_content(response: Response, expected_response_content):
        assert response.content.decode("utf-8") == expected_response_content, f"Unexpected response content. Content is {response.content}. Expected content is {expected_response_content}"

    staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}"
        
        assert name in response_as_dict, f"Response json doesn't have key {name}"
    
    staticmethod
    def assert_json_has_keys(response: Response, names):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}"
        
        for name in names:
            assert name in response_as_dict, f"Response json doesn't have key {name}"    
        
    staticmethod
    def assert_json_has_no_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}"
        
        assert name not in response_as_dict, f"Response json shouldn't have key {name}. But it's present"

    staticmethod
    def assert_json_has_no_keys(response: Response, names):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}"
        
        for name in names:
            assert name not in response_as_dict, f"Response json shouldn't have key {name}. But it's present"