class Vacancy:
    """Класс для создания объекта типа Вакансия"""
    __slots__ = ('name', 'url', 'salary', 'experience')

    name: str
    url: str
    salary: (int, str, dict, None)
    experience: str

    def __init__(self, name, url, salary, experience):
        self.name = name if isinstance(name, str) else 'Неверный формат'
        self.url = url if isinstance(url, str) else 'Неверный формат'
        self.experience = experience if isinstance(experience, (str, int)) else 'Неверный формат'
        self.salary = salary if isinstance(salary, (str, int, dict, None)) else 'Неверный формат'

    def __eq__(self, other):
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        else:
            raise TypeError('Можно сравнивать только объекты класса Vacancy')

    def __ne__(self, other):
        if isinstance(other, Vacancy):
            return self.salary != other.salary
        else:
            raise TypeError('Можно сравнивать только объекты класса Vacancy')

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        else:
            raise TypeError('Можно сравнивать только объекты класса Vacancy')

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        else:
            raise TypeError('Можно сравнивать только объекты класса Vacancy')

    def __le__(self, other):
        if isinstance(other, Vacancy):
            return self.salary <= other.salary
        else:
            raise TypeError('Можно сравнивать только объекты класса Vacancy')

    def __ge__(self, other):
        if isinstance(other, Vacancy):
            return self.salary >= other.salary
        else:
            raise TypeError('Можно сравнивать только объекты класса Vacancy')

    @classmethod
    def cast_to_object_list(cls, json_data):
        """Преобразует набор данных из JSON в список объектов"""

        result = [cls(vacancy['name'],
                      vacancy['alternate_url'],
                      vacancy['experience']['name'],
                      vacancy['salary'],
                      ) for vacancy in json_data]

        return result

    @classmethod
    def cast_to_object_dict(cls, vacancies):
        """Принимает список объектов Vacancy и преобразовывает в словарь"""

        if type(vacancies) is cls:
            return {
                "name": vacancies.name,
                "url": vacancies.url,
                "salary": vacancies.salary,
                "experience": vacancies.experience
            }
        else:
            return [
                {
                    "name": vacancy.name,
                    "url": vacancy.url,
                    "salary": vacancy.salary,
                    "experience": vacancy.experience
                } for vacancy in vacancies
            ]

    @staticmethod
    def get_unique_vacancy(current_data, new_data):
        """Проверяет наличие вакансии в """
        if type(new_data) == dict:
            new_data = [new_data]
        for c_data in current_data:
            for n_data in new_data:
                if n_data['url'] == c_data['url']:
                    new_data.remove(n_data)

        return new_data

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
        pass
