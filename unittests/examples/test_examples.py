import pytest


def test_string_reverse():

    # Arrange
    original_string = 'hello'

    # Act
    reverse = reverse_string(original_string)

    # Assert
    assert reverse == 'olleh'


def test_string_length():

    # Arrange
    string_to_test = 'test'

    # Arrange and act
    length = string_length(string_to_test)

    # Assert
    assert length == 4


def test_count_occurrences():

    # Arrange
    string_with_cs = 'cucumber'

    # Act
    count = count_occurrences(string_with_cs, 'c')

    # Assert
    assert count > 1


def test_raise_error():

    # Arrange
    string_that_raises_an_error = 'test for errors'

    # Arrange, act, assert
    with pytest.raises(ValueError):
        raise_error(string_that_raises_an_error)


testdata_string_reverse = [
    ('world', 'dlrow'),
    ('banana', 'ananab'),
    ('maserati', 'itaresam')
]


@pytest.mark.parametrize("normal, expected_reverse", testdata_string_reverse)
def test_reverse(normal, expected_reverse):

    actual_reverse = reverse_string(normal)

    assert actual_reverse == expected_reverse


def string_length(string):
    return len(string)


def count_occurrences(string, char):
    return string.count(char)


def reverse_string(string):
    return string[::-1]


def raise_error(string):
    raise ValueError('I will not accept ' + string + ' as a parameter')
