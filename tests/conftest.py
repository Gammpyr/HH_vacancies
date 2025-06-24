import pytest

from src.vacancy import Vacancy

@pytest.fixture
def data_test():
    return [
        Vacancy('','','', {'from': 20000},''),
        Vacancy('','','', {'from': 10000},''),
        Vacancy('','','', {'from': 30000},'')]


@pytest.fixture
def fake_vacancy():
    return Vacancy('Тестировщик',
                   'www.test.err',
                   'Errors',
                   {'from': 1, 'to':10},
                   'Find and resolve errors')

@pytest.fixture
def fake_vacancy2():
    return Vacancy('Тестировщик2',
                   'www.test.err2',
                   'Errors2',
                   {'from': 2, 'to':20},
                   'Find and resolve errors2')

@pytest.fixture
def fake_vacancy3():
    return Vacancy('Тестировщик3',
                   'www.test.err3',
                   'Errors3',
                   {'from': 2, 'to':30},
                   'Find and resolve errors3')

@pytest.fixture
def fake_vacancy4():
    return Vacancy('None',
                   'None',
                   'None',
                   None,
                   'None')

@pytest.fixture
def fake_request_dict():
    result = {"name": "Manual QA Engineer",
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
                 }

@pytest.fixture
def fake_request():
    result = {
        "items":
            [
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
    }

    return result
