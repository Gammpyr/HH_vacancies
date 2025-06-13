

class Vacancy:
    """Класс для создания объекта типа Вакансия"""

    def __init__(self, name, url, salary, experience):
        self.name = name
        self.url = url
        self.salary = salary
        self.experience = experience

    @classmethod
    def cast_to_object_list(cls, json_data):
        """Преобразовывает данные из JSON в список объектов"""
        result = [cls(vacancy['name'],
                      vacancy['url'],
                      vacancy['salary'],
                      vacancy['experience']['name']) for vacancy in json_data]

        return result

    @staticmethod
    def filter_vacancies(vacancies: list, keywords: list):
        """Фильтрует вакансии по ключевому слову"""
        pass

    @staticmethod
    def get_vacancies_by_salary(vacancies, salary_range):
        """Возвращает список вакансий в указанном диапазоне зарплат"""
        pass

    @staticmethod
    def sort_vacancies(vacancies):
        """Сортирует вакансии по убыванию зарплат"""
        pass

    @staticmethod
    def get_top_vacancies(vacancies, top_n):
        """Возвращает топ-n вакансий по зарплате"""
        pass

    @staticmethod
    def print_vacancies(vacancies):
        """Принимает список объектов Vacancy и преобразовывает в словарь"""
        result = [
            {'name': vacancy.name,
             'url': vacancy.url,
             'salary': {
                 'from': vacancy.salary.get('from', None) if vacancy.salary is not None else None,
                 'to': vacancy.salary.get('to', None) if vacancy.salary is not None else None,
                 'currency': vacancy.salary['currency'] if vacancy.salary is not None else None
             },
             'experience': vacancy.experience} for vacancy in vacancies
        ]

        return result
