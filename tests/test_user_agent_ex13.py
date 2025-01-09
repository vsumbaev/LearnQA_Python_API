import requests
import pytest
import json

class TestUserAgent:
    user_agents = [{'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30':['Mobile','No','Android']},
                  {'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1':['Mobile','Chrome','iOS']},
                  {'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)':['Googlebot','Unknown','Unknown']},
                  {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0':['Web','Chrome','No']},
                  {'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1':['Mobile','No','iPhone']}]
    @pytest.mark.parametrize('user_agent', user_agents)
    def test_user_agent_ex13(self, user_agent):
        # Get key from dict
        user_agent_key_value_list=list(user_agent.keys())
        user_agent_key_value_str=''.join(user_agent_key_value_list)
        # Get list with expected values from dict
        user_agent_value_list=list(user_agent.get(user_agent_key_value_str))
        # Get response 
        headers = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                           headers={"User-Agent":user_agent_key_value_str}).text
        # Make list with values from response
        values_got_from_response = []
        values_got_from_response.append(json.loads(headers)["platform"])
        values_got_from_response.append(json.loads(headers)["browser"])
        values_got_from_response.append(json.loads(headers)["device"])
        # Assert values 
        assert values_got_from_response == user_agent_value_list
