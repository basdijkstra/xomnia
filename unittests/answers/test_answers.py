import pytest


# Exercise 1
# Create a test method that calls the add(x, y) method defined below
# Pass it the parameter values 2 and 3
# Perform an assert to check that the result equals 5
def test_add_two_and_three():

    # Arrange and act
    result = add(2, 3)

    # Assert
    assert result == 5


# Exercise 2
# Create a test method that calls the divide(x, y) method defined below
# Pass 0 as the second argument and check that this method raises a ZeroDivisionError
def test_divide_throws_zerodivisionerror():

    with pytest.raises(ZeroDivisionError):
        divide(9, 0)


# Exercise 3a
# Create a test data object that contains at least three sets of test data for the multiply method
# Use the format (first_number, second_number, expected_result)
testdata_multiply = [
    (4, 5, 20),
    (3, 6, 18),
    (99, 99, 9801)
]


# Exercise 3b
# Create a test method that calls the multiply(x, y) method of the Calculator
# Use the test data object you created to parameterize the test
# Pass the first two fields of the test data object as parameters to the multiply method
# Use the third field of the test data object as the expected outcome in the assert
@pytest.mark.parametrize("first, second, expected_result", testdata_multiply)
def test_multiply(first, second, expected_result):

    actual_result = multiply(first, second)
    assert actual_result == expected_result


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def subtract(x, y):
    return x - y


def divide(x, y):
    return x / y
