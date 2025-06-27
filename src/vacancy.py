from typing import Any


class Vacancy:
    """Класс для создания объекта типа Вакансия"""

    __slots__ = ("name", "url", "salary", "experience", "description")

    name: str
    url: str
    experience: str
    salary: (dict, int)
    description: str

    def __init__(self, name: str, url: str, experience: str, salary: dict | int, description: str) -> None:
        self.name = self.__validate_name(name)
        self.url = self.__validate_url(url)
        self.experience = self.__validate_experience(experience)
        self.salary = self.__validate_salary(salary)
        self.description = self.__validate_description(description)

    def __eq__(self, other: Any) -> Any:
        if isinstance(other, Vacancy) and isinstance(self, Vacancy):
            if self.salary is not None and other.salary is not None:
                return self.salary["from"] == other.salary["from"]
            else:
                return "Не указана зарплата"
        else:
            raise TypeError("Можно сравнивать только объекты класса Vacancy")

    def __ne__(self, other: Any) -> Any:
        if isinstance(other, Vacancy) and isinstance(self, Vacancy):
            if self.salary is not None and other.salary is not None:
                return self.salary["from"] != other.salary["from"]
            else:
                return "Не указана зарплата"
        else:
            raise TypeError("Можно сравнивать только объекты класса Vacancy")

    def __lt__(self, other: Any) -> Any:
        if isinstance(other, Vacancy) and isinstance(self, Vacancy):
            if self.salary is not None and other.salary is not None:
                return self.salary["from"] < other.salary["from"]
            else:
                return "Не указана зарплата"
        else:
            raise TypeError("Можно сравнивать только объекты класса Vacancy")

    def __gt__(self, other: Any) -> Any:
        if isinstance(other, Vacancy) and isinstance(self, Vacancy):
            if self.salary is not None and other.salary is not None:
                return self.salary["from"] > other.salary["from"]
            else:
                return "Не указана зарплата"
        else:
            raise TypeError("Можно сравнивать только объекты класса Vacancy")

    def __le__(self, other: Any) -> Any:
        if isinstance(other, Vacancy) and isinstance(self, Vacancy):
            if self.salary is not None and other.salary is not None:
                return self.salary["from"] <= other.salary["from"]
            else:
                return "Не указана зарплата"
        else:
            raise TypeError("Можно сравнивать только объекты класса Vacancy")

    def __ge__(self, other: Any) -> Any:
        if isinstance(other, Vacancy) and isinstance(self, Vacancy):
            if self.salary is not None and other.salary is not None:
                return self.salary["from"] >= other.salary["from"]
            else:
                return "Не указана зарплата"
        else:
            raise TypeError("Можно сравнивать только объекты класса Vacancy")

    def __validate_name(self, name: str) -> str:
        """Валидация названия вакансии"""
        if not isinstance(name, str):
            raise TypeError("Название вакансии должно быть строкой")
        if not name.split():
            raise ValueError("Название вакансии не должно быть пустым")

        return name

    def __validate_url(self, url: str) -> str:
        """Валидация URL вакансии"""
        if not isinstance(url, str):
            raise TypeError("URL вакансии должен быть строкой")
        if not url.startswith(('http://', 'https://', 'www.')):
            raise ValueError("URL должен начинаться с http://, https:// или www")

        return url

    def __validate_experience(self, experience: str) -> str:
        """Валидация опыта работы"""
        if not isinstance(experience, str):
            raise TypeError("Опыт работы должен быть строкой")
        if not experience.strip():
            raise ValueError("Опыт работы не должен быть пустым")

        return experience

    def __validate_salary(self, salary: dict | int) -> dict:
        """Валидация данных о зарплате"""

        if isinstance(salary, type(None)):
            return {'from': None, 'to': None, 'currency': None}

        if isinstance(salary, (int, float)):
            return {'from': salary, 'to': None, 'currency': 'RUR'}

        if not isinstance(salary, dict):
            raise TypeError("Зарплата должна быть представлена словарем")

        if 'from' in salary and not isinstance(salary['from'], (int, float, type(None))):
            raise TypeError("Зарплата 'from' должна быть числом или None")

        if 'to' in salary and not isinstance(salary['to'], (int, float, type(None))):
            raise TypeError("Зарплата 'to' должна быть числом или None")

        if 'currency' in salary and not isinstance(salary['currency'], (str, type(None))):
            raise TypeError("Валюта должна быть строкой или None")

        return salary


    def __validate_description(self, description: str) -> str:
        """Валидация описания вакансии"""
        if not isinstance(description, str):
            raise TypeError("Описание вакансии должно быть строкой")
        if not description.split():
            raise ValueError("Описание вакансии не должно быть пустым")

        return description



    @classmethod
    def cast_to_object_list(cls, json_data: dict | list) -> list:
        """Преобразует набор данных из JSON в список объектов"""

        result = [
            cls(
                vacancy["name"],
                vacancy["alternate_url"],
                vacancy["experience"]["name"],
                vacancy["salary"] if vacancy["salary"] is not None else {"from": 0, "to": 0, "currency": None},
                vacancy["snippet"]["responsibility"],
            )
            for vacancy in json_data
        ]

        return result

    @classmethod
    def cast_to_object_dict(cls, vacancies: Any) -> list | dict:
        """Принимает список объектов Vacancy и преобразовывает в словарь"""

        if type(vacancies) is cls:
            return {
                "name": vacancies.name,
                "url": vacancies.url,
                "salary": vacancies.salary,
                "experience": vacancies.experience,
                "description": vacancies.description,
            }
        else:
            return [
                {
                    "name": vacancy.name,
                    "url": vacancy.url,
                    "salary": vacancy.salary,
                    "experience": vacancy.experience,
                    "description": vacancy.description,
                }
                for vacancy in vacancies
            ]

    @staticmethod
    def get_unique_vacancy(current_data: list, new_data: Any) -> Any:
        """Отфильтровывает вакансии new_data находящиеся в current_data"""
        if type(new_data) is dict:
            new_data = [new_data]
        for c_data in current_data:
            for n_data in new_data:
                if n_data["url"] == c_data["url"]:
                    new_data.remove(n_data)

        return new_data

    @staticmethod
    def get_vacancies_by_salary(vacancies: list, salary_from: int, salary_to: str) -> list:
        """Возвращает список вакансий в указанном диапазоне зарплат"""
        if salary_to == "":
            return [
                vacancy
                for vacancy in vacancies
                if vacancy.salary is not None
                and vacancy.salary.get("from") is not None
                and salary_from <= vacancy.salary.get("from", 0)
            ]
        else:
            return [
                vacancy
                for vacancy in vacancies
                if vacancy.salary is not None
                and vacancy.salary.get("from") is not None
                and salary_from <= vacancy.salary.get("from", 0) <= int(salary_to)
            ]

    @staticmethod
    def sort_vacancies(vacancies: list) -> list:
        """Сортирует вакансии по убыванию зарплат"""
        return sorted(vacancies, key=lambda x: x.salary["from"], reverse=True)

    @staticmethod
    def get_top_vacancies(vacancies: list, top_n: int) -> list:
        """Возвращает топ-n вакансий по зарплате"""
        return vacancies[:top_n]

    @staticmethod
    def print_vacancies(vacancies: list) -> None:
        vacancy_list = Vacancy.cast_to_object_dict(vacancies)

        for i in range(len(vacancy_list)):
            print(f"\n{i + 1}. {vacancy_list[i]['name']}")
            print(vacancy_list[i]["url"])
            print(f"{vacancy_list[i]['description']}")
            print(
                f"Зарплата: "
                f"От: {vacancy_list[i]['salary']['from']} "
                f"До: {vacancy_list[i]['salary']['to']} "
                f"Валюта: {vacancy_list[i]['salary']['currency']}"
            )
            print(f"Требуется опыт: {vacancy_list[i]['experience']}")
