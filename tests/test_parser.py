from unittest.mock import patch, MagicMock

import pytest
import requests

from src.parser import HeadHunterAPI, Parser


@patch('requests.get')
def test_hh_api(mock_requests, fake_request):
    mock_requests.return_value.json.return_value = fake_request
    mock_requests.return_value.status_code = 200
    hh_api = HeadHunterAPI()
    hh_data = hh_api.get_vacancies('python')

    assert hh_data == fake_request['items'] * 20

@patch('requests.get')
def test_hh_api_error(mock_requests, fake_request):
    mock_requests.return_value.json.return_value = fake_request

    with pytest.raises(requests.RequestException):
        hh_api = HeadHunterAPI()
        hh_api.get_vacancies('python')
