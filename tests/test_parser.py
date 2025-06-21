from unittest.mock import patch

from src.parser import HeadHunterAPI

@patch('src.requests.get')
def test_hh_api(mock_get, fake_request):
    hh_api = HeadHunterAPI()

    hh_api.get_vacancies()