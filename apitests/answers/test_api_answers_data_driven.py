import pytest
import requests

# Exercise 2.1
# Create a test data object test_data_users
# with three lines / test cases:
# id -             name -           city
#  1 -    Leanne Graham -    Gwenborough
#  4 - Patricia Lebsack -    South Elvis
#  9 -  Glenna Reichert - Bartholomebury
test_data_users = [
    (1, "Leanne Graham", "Gwenborough"),
    (4, "Patricia Lebsack", "South Elvis"),
    (9, "Glenna Reichert", "Bartholomebury")
]


# Exercise 2.2
# Write a parameterized test that retrieves user data using
# a GET call to https://jsonplaceholder.typicode.com/users/<user_id>
# and checks that the 'name' and the 'city' elements correspond to those
# that are specified in the test data object
@pytest.mark.parametrize("user_id, expected_name, expected_city", test_data_users)
def test_get_user_data_check_name_and_city(user_id, expected_name, expected_city):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    response_body = response.json()
    assert response_body["name"] == expected_name
    assert response_body["address"]["city"] == expected_city
