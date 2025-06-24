import pytest

from src.vacancy import Vacancy


def test_vacancy(fake_vacancy):
    assert fake_vacancy.name == 'Тестировщик'
    assert fake_vacancy.url == 'www.test.err'
    assert fake_vacancy.experience == 'Errors'
    assert fake_vacancy.salary == {'from': 1, 'to': 10}
    assert fake_vacancy.description == 'Find and resolve errors'


def test_vacancy_eq(fake_vacancy, fake_vacancy2, fake_vacancy3, fake_vacancy4):
    assert (fake_vacancy == fake_vacancy2) is False
    assert (fake_vacancy2 == fake_vacancy3) is True
    assert (fake_vacancy3 == fake_vacancy4) == 'Не указана зарплата'
    with pytest.raises(TypeError):
        a = fake_vacancy == 10


def test_vacancy_ne(fake_vacancy, fake_vacancy2, fake_vacancy3, fake_vacancy4):
    assert (fake_vacancy != fake_vacancy2) is True
    assert (fake_vacancy2 != fake_vacancy3) is False
    assert (fake_vacancy3 != fake_vacancy4) == 'Не указана зарплата'
    with pytest.raises(TypeError):
        a = fake_vacancy != 10


def test_vacancy_lt(fake_vacancy, fake_vacancy2, fake_vacancy3, fake_vacancy4):
    assert (fake_vacancy < fake_vacancy2) is True
    assert (fake_vacancy2 < fake_vacancy) is False
    assert (fake_vacancy2 < fake_vacancy3) is False
    assert (fake_vacancy3 < fake_vacancy4) == 'Не указана зарплата'
    with pytest.raises(TypeError):
        a = fake_vacancy < 10


def test_vacancy_gt(fake_vacancy, fake_vacancy2, fake_vacancy3, fake_vacancy4):
    assert (fake_vacancy > fake_vacancy2) is False
    assert (fake_vacancy2 > fake_vacancy) is True
    assert (fake_vacancy2 > fake_vacancy3) is False
    assert (fake_vacancy3 > fake_vacancy4) == 'Не указана зарплата'
    with pytest.raises(TypeError):
        a = fake_vacancy > 10


def test_vacancy_le(fake_vacancy, fake_vacancy2, fake_vacancy3, fake_vacancy4):
    assert (fake_vacancy <= fake_vacancy2) is True
    assert (fake_vacancy2 <= fake_vacancy) is False
    assert (fake_vacancy2 <= fake_vacancy3) is True
    assert (fake_vacancy3 <= fake_vacancy4) == 'Не указана зарплата'
    with pytest.raises(TypeError):
        a = fake_vacancy <= 10


def test_vacancy_ge(fake_vacancy, fake_vacancy2, fake_vacancy3, fake_vacancy4):
    assert (fake_vacancy >= fake_vacancy2) is False
    assert (fake_vacancy2 >= fake_vacancy3) is True
    assert (fake_vacancy2 >= fake_vacancy) is True
    assert (fake_vacancy3 >= fake_vacancy4) == 'Не указана зарплата'
    with pytest.raises(TypeError):
        a = fake_vacancy >= 10


def test_cast_to_object_list(fake_request):
    result = Vacancy.cast_to_object_list(fake_request["items"])
    assert result[0].name == "Manual QA Engineer"
    assert result[0].url == "https://hh.ru/vacancy/121726350"
    assert result[1].name == "Senior QA Engineer"
    assert result[1].url == "https://hh.ru/vacancy/121727303"


def test_cast_to_object_dict_list(fake_request):
    objects_list = Vacancy.cast_to_object_list(fake_request["items"])
    result = Vacancy.cast_to_object_dict(objects_list)
    assert result[0]['name'] == "Manual QA Engineer"
    assert result[0]['url'] == "https://hh.ru/vacancy/121726350"
    assert result[1]['name'] == "Senior QA Engineer"
    assert result[1]['url'] == "https://hh.ru/vacancy/121727303"


def test_cast_to_object_dict(fake_request):
    objects_list = Vacancy.cast_to_object_list(fake_request['items'])
    result = Vacancy.cast_to_object_dict(objects_list[0])
    assert result['name'] == "Manual QA Engineer"
    assert result['url'] == "https://hh.ru/vacancy/121726350"

def test_get_unique_vacancy_dict():
    result = Vacancy.get_unique_vacancy({},{})
    assert result == [{}]

def test_get_unique_vacancy():

    test_data1 = [
        {"url": "https://hh.ru/vacancy/121726350"},
        {"url": "https://hh.ru/vacancy/121727303"}
    ]

    test_data2 = [
        {"url": "https://hh.ru/vacancy/121726350"},
        {"url": "https://hh.ru/"}
    ]

    result = Vacancy.get_unique_vacancy(test_data1, test_data2)

    assert result == [{"url": "https://hh.ru/"}]

def test_sort_vacancies(data_test):
    result = Vacancy.sort_vacancies(data_test)
    expected = [data_test[2], data_test[0], data_test[1]]
    assert result == expected

def test_get_top_vacancies(data_test):
    result = Vacancy.get_top_vacancies(data_test, 2)
    expected = [data_test[0], data_test[1]]

    assert result == expected