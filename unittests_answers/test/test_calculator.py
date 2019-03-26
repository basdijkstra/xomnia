import pytest
from unittests import calculator


# Exercise 1
# Create a test method that calls the add(x, y) method of the Calculator
# Perform an assert to check that the result equals 5
def test_add():

    calc = calculator.Calculator

    result = calc.add(2, 3)
    assert result == 5


# Exercise 2
# Create a test method that calls the divide(x, y) method of the Calculator
# Pass 0 as the second argument and check that this method raises a ZeroDivisionError
def test_zero_division():

    calc = calculator.Calculator

    with pytest.raises(ZeroDivisionError):
        calc.divide(4, 0)


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

    calc = calculator.Calculator

    actual_result = calc.multiply(first, second)
    assert actual_result == expected_result
