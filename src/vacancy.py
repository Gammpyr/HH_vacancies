from typing import Any


class Vacancy:
    """Класс для создания объекта типа Вакансия"""
    __slots__ = ('name', 'url', 'salary', 'experience', 'description')

    name: str
    url: str
    salary: [int, str, dict, None]
    experience: str
    description: str

    def __init__(self, name, url, experience, salary, description):
        self.name = name if isinstance(name, str) else 'Неверный формат'
        self.url = url if isinstance(url, str) else 'Неверный формат'
        self.experience = experience if isinstance(experience, (str, int)) else 'Неверный формат' #else experience['name'] if isinstance(experience, dict)
        self.salary = salary if isinstance(salary, (dict, type(None))) else 'Неверный формат'
        self.description = description if isinstance(description, (str, int)) else 'Неверный формат'

    def __eq__(self, other):
        if isinstance(other, Vacancy) and isinstance(self, Vacancy):
            if self.salary is not None and other.salary is not None:
                return self.salary['from'] == other.salary['from']
            else:
                return 'Не указана зарплата'
        else:
            raise TypeError('Можно сравнивать только объекты класса Vacancy')

    def __ne__(self, other):
        if isinstance(other, Vacancy) and isinstance(self, Vacancy):
            if self.salary is not None and other.salary is not None:
                return self.salary['from'] != other.salary['from']
            else:
                return 'Не указана зарплата'
        else:
            raise TypeError('Можно сравнивать только объекты класса Vacancy')

    def __lt__(self, other):
        if isinstance(other, Vacancy) and isinstance(self, Vacancy):
            if self.salary is not None and other.salary is not None:
                return self.salary['from'] < other.salary['from']
            else:
                return 'Не указана зарплата'
        else:
            raise TypeError('Можно сравнивать только объекты класса Vacancy')

    def __gt__(self, other):
        if isinstance(other, Vacancy) and isinstance(self, Vacancy):
            if self.salary is not None and other.salary is not None:
                return self.salary['from'] > other.salary['from']
            else:
                return 'Не указана зарплата'
        else:
            raise TypeError('Можно сравнивать только объекты класса Vacancy')

    def __le__(self, other):
        if isinstance(other, Vacancy) and isinstance(self, Vacancy):
            if self.salary is not None and other.salary is not None:
                return self.salary['from'] <= other.salary['from']
            else:
                return 'Не указана зарплата'
        else:
            raise TypeError('Можно сравнивать только объекты класса Vacancy')

    def __ge__(self, other):
        if isinstance(other, Vacancy) and isinstance(self, Vacancy):
            if self.salary is not None and other.salary is not None:
                return self.salary['from'] >= other.salary['from']
            else:
                return 'Не указана зарплата'
        else:
            raise TypeError('Можно сравнивать только объекты класса Vacancy')

    @classmethod
    def cast_to_object_list(cls, json_data: dict | list):
        """Преобразует набор данных из JSON в список объектов"""

        result = [cls(vacancy['name'],
                      vacancy['alternate_url'],
                      vacancy['experience']['name'],
                      vacancy['salary'] if vacancy['salary'] is not None else {"from": 0, "to": 0, "currency": None},
                      vacancy['snippet']['responsibility']) for vacancy in json_data]

        return result

    @classmethod
    def cast_to_object_dict(cls, vacancies: Any):
        """Принимает список объектов Vacancy и преобразовывает в словарь"""

        if type(vacancies) is cls:
            return {
                "name": vacancies.name,
                "url": vacancies.url,
                "salary": vacancies.salary,
                "experience": vacancies.experience,
                "description": vacancies.description
            }
        else:
            return [
                {
                    "name": vacancy.name,
                    "url": vacancy.url,
                    "salary": vacancy.salary,
                    "experience": vacancy.experience,
                    "description": vacancy.description
                } for vacancy in vacancies
            ]

    @staticmethod
    def get_unique_vacancy(current_data: dict | list, new_data: dict | list):
        """Отфильтровывает вакансии new_data находящиеся в current_data"""
        if type(new_data) == dict:
            new_data = [new_data]
        for c_data in current_data:
            for n_data in new_data:
                if n_data['url'] == c_data['url']:
                    new_data.remove(n_data)

        return new_data

    @staticmethod
    def get_vacancies_by_salary(vacancies: list, salary_from: int, salary_to: str):
        """Возвращает список вакансий в указанном диапазоне зарплат"""
        if salary_to == '':
            return [vacancy for vacancy in vacancies
                    if vacancy.salary is not None
                    and vacancy.salary.get('from') is not None
                    and salary_from <= vacancy.salary.get('from', 0)]
        else:
            return [vacancy for vacancy in vacancies
                    if vacancy.salary is not None
                    and vacancy.salary.get('from') is not None
                    and salary_from <= vacancy.salary.get('from', 0) <= int(salary_to)]

    @staticmethod
    def sort_vacancies(vacancies: list):
        """Сортирует вакансии по убыванию зарплат"""
        return sorted(vacancies, key=lambda x: x.salary['from'], reverse=True)

    @staticmethod
    def get_top_vacancies(vacancies, top_n):
        """Возвращает топ-n вакансий по зарплате"""
        return vacancies[:top_n]

    @staticmethod
    def print_vacancies(vacancies: list):
        vacancy_list = Vacancy.cast_to_object_dict(vacancies)

        for i in range(len(vacancy_list)):
            print(f'\n{i + 1}. {vacancy_list[i]['name']}')
            print(vacancy_list[i]['url'])
            print(f'{vacancy_list[i]['description']}')
            print(f"Зарплата: От: {vacancy_list[i]['salary']['from']} До: {vacancy_list[i]['salary']['to']} Валюта: {vacancy_list[i]['salary']['currency']}")
            print(f"Требуется опыт: {vacancy_list[i]['experience']}")

