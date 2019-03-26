import pytest
from unittests import stringutil


def test_string_reverse():

    su = stringutil.StringUtil

    reverse = su.reverse_string('hello')

    assert reverse == 'olleh'


def test_string_length():

    # Arrange
    su = stringutil.StringUtil

    # Act
    length = su.string_length('test')

    # Assert
    assert length == 4


def test_count_occurrences():

    # Arrange
    su = stringutil.StringUtil

    # Act
    count = su.count_occurrences('cucumber', 'c')

    # Assert
    assert count > 1


def test_raise_error():

    su = stringutil.StringUtil

    with pytest.raises(ValueError):
        su.raise_error('test for errors')


testdata_string_reverse = [
    ('world', 'dlrow'),
    ('banana', 'ananab'),
    ('maserati', 'itaresam')
]


@pytest.mark.parametrize("normal, expected_reverse", testdata_string_reverse)
def test_multiply(normal, expected_reverse):

    su = stringutil.StringUtil

    actual_reverse = su.reverse_string(normal)

    assert actual_reverse == expected_reverse
