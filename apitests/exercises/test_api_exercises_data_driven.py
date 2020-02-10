import pytest
import requests

# Exercise 2.1
# Create a test data object test_data_users
# with three lines / test cases:
# id -             name -           city
#  1 -    Leanne Graham -    Gwenborough
#  4 - Patricia Lebsack -    South Elvis
#  9 -  Glenna Reichert - Bartholomebury


# Exercise 2.2
# Write a parameterized test that retrieves user data using
# a GET call to https://jsonplaceholder.typicode.com/users/<user_id>
# and checks that the 'name' and the 'city' elements correspond to those
# that are specified in the test data object
