from abc import ABC, abstractmethod
from typing import Any

import requests


class Parser(ABC):

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list:
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self) -> None:
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params: dict[str, Any] = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies: list = []

    def get_vacancies(self, keyword: str) -> list:

        self.__params["text"] = keyword

        while self.__params.get("page") != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code != 200:
                raise requests.RequestException

            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

        return self.__vacancies
