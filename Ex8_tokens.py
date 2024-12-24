import requests
import time
import json
URL="https://playground.learnqa.ru/ajax/api/longtime_job"

#1
make_task_response = requests.get(URL)
make_task_response_body = make_task_response.json()
token_task = make_task_response_body["token"]
time_to_delay_for_task = make_task_response_body["seconds"]
#2
task_not_exists_response = requests.get(URL, params={"token":token_task})
task_not_exists_response_body = task_not_exists_response.json()
assert task_not_exists_response_body["status"] == "Job is NOT ready"
#3
time.sleep(int(time_to_delay_for_task))
task_done_check_response = requests.get(URL, params={"token":token_task})
task_done_check_response_body = task_done_check_response.json()
print(task_done_check_response_body)
assert(task_done_check_response_body["status"] == "Job is ready" and "result" in task_done_check_response_body)
