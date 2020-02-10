import pytest
import requests
test_data_zip = [
    ("us", "90210", "Beverly Hills"),
    ("us", "12345", "Schenectady"),
    ("ca", "B2A", "North Sydney South Central")
]


@pytest.mark.parametrize("country_code, zip_code, expected_place", test_data_zip)
def test_get_location_data_check_place_name(country_code, zip_code, expected_place):
    response = requests.get(f'http://api.zippopotam.us/{country_code}/{zip_code}')
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place
