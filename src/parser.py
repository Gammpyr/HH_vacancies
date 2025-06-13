import json
from abc import ABC, abstractmethod
from pathlib import Path

import requests


class Parser(ABC):
    pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keyword):
        ## сбросить счётчик страниц на 0?
        self.params['text'] = keyword

        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

        return self.vacancies

    def save_to_file(self, filename='hh'):
        filepath = Path('./data/') / Path(f'{filename}.json')
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(self.vacancies, file, indent=4, ensure_ascii=False)


# class JSONSaver:
#     """Сохраняет объект в Json файл в .data/filename.json"""
#     def __init__(self):
#         self.datapath = Path('./data/')
#
#     def save_to_file(self, data, filename='hh'):
#         filepath = self.datapath / Path(f'{filename}.json')
#         with open(filepath, 'w', encoding='utf-8') as file:
#             json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    hh1 = HeadHunterAPI()
    hh1.get_vacancies('python')
    hh1.save_to_file('python_test1')

    # save_to_json = JSONSaver()
    # save_to_json.save_to_file(hh1.vacancies, 'python_test2')
