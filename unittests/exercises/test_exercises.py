import pytest


# Exercise 1
# Create a test method that calls the add(x, y) method defined below
# Perform an assert to check that the result equals 5


# Exercise 2
# Create a test method that calls the divide(x, y) method defined below
# Pass 0 as the second argument and check that this method raises a ZeroDivisionError


# Exercise 3a
# Create a test data object that contains at least three sets of test data for the multiply method
# Use the format (first_number, second_number, expected_result)

# Exercise 3b
# Create a test method that calls the multiply(x, y) method defined below
# Use the test data object you created to parameterize the test
# Pass the first two fields of the test data object as parameters to the multiply method
# Use the third field of the test data object as the expected outcome in the assert


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def subtract(x, y):
    return x - y


def divide(x, y):
    return x / y
