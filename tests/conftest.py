import pytest


@pytest.fixture
def fake_request():
    result = [
        {"name": "Manual QA Engineer",
         "salary": {
             "from": 80000,
             "to": 120000,
             "currency": "RUR",
             "gross": False
         },
         "alternate_url": "https://hh.ru/vacancy/121726350",
         "snippet": {
             "responsibility": "Тестирование web/backend. Написание и актуализация тестовой документации. Регистрация дефектов и контроль их устранения. Проверка реализованых задач на деве. "},
         "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"}
         },
        {"name": "Senior QA Engineer",
         "salary": None,
         "alternate_url": "https://hh.ru/vacancy/121727303",
         "snippet": {
             "responsibility": "Тестировать новые модули и функции продукта. Участвовать в построении процесса тестирования (регресс, смоук, тестирование фичей, процесс выкатки, ретроспектива релиза). "
         },
         "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"}
         }
    ]

    return result
