import requests


# Exercise 1.1
# Perform a GET request to https://jsonplaceholder.typicode.com/users/1
# Check that the response status code equals 200
def test_get_user_with_id_1_check_status_code_equals_200():
    response = requests.get("http://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200


# Exercise 1.2
# Perform a GET request to https://jsonplaceholder.typicode.com/users/1
# Check that the value of the response header 'Content-Type' equals 'application/json; charset=utf-8'
def test_get_user_with_id_1_check_content_type_equals_json():
    response = requests.get("http://jsonplaceholder.typicode.com/users/1")
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"


# Exercise 1.3
# Perform a GET request to https://jsonplaceholder.typicode.com/users/1
# Check that the response body element 'name' has a value equal to 'Leanne Graham'
def test_get_user_with_id_1_check_name_equals_leanne_graham():
    response = requests.get("http://jsonplaceholder.typicode.com/users/1")
    response_body = response.json()
    assert response_body["name"] == "Leanne Graham"
