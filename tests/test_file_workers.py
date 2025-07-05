from unittest.mock import patch

from src.file_workers import JSONSaver

json_file = '{"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"},},}'
json_saver = JSONSaver()


@patch("builtins.open")
def test_get_data_from_file(mock_file):
    mock_file.return_value.__enter__.return_value.read.return_value = '{"some": "data"}'

    assert json_saver.get_data_from_file() == {"some": "data"}


def test_get_data_from_file_fnf_error():
    assert json_saver.get_data_from_file("Fake_file_name") == []


@patch("builtins.open")
def test_get_data_from_file_json_decoder_error(mock_file):
    mock_file.return_value.__enter__.return_value.read.return_value = "invalid { json }"

    assert json_saver.get_data_from_file() == []


@patch("builtins.open")
def test_delete_vacancy(mock_file):
    mock_file.return_value.__enter__.return_value.read.return_value = "invalid { json }"
    json_saver.delete_vacancy("filepath")


def test_delete_vacancy_error():
    with patch("builtins.open", side_effect=FileNotFoundError):
        with patch("builtins.print") as mock_print:
            json_saver.delete_vacancy("fake_file_name")
            mock_print.assert_called_once_with("Такого файла не существует")


# @patch('src.file_workers.JSONSaver.get_data_from_file')
# def test_add_vacancy(mock_data, fake_vacancy, fake_request):
#     mock_data = MagicMock()
#     mock_data.return_value = fake_request
#
#     json_saver.add_vacancy(fake_vacancy, 'fake_file')


# @patch("builtins.open", new_callable=mock_open)

# json_file = [{"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"},},}]
# @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(json_file))
