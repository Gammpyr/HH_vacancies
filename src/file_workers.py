import json
from pathlib import Path

from src.vacancy import Vacancy


class JSONSaver:
    """Класс для сохранения в JSON-файл"""

    def __init__(self):
        self.datapath = Path('./data/')

    def save_to_file(self, data, filename='hh'):
        filepath = self.datapath / Path(f'{filename}.json')

        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


    def add_vacancy(self, data: Vacancy | list[dict], filename: str='hh'):
        filepath = self.datapath / Path(f'{filename}.json')

        if isinstance(data, Vacancy):
            data = Vacancy.cast_to_object_dict([data])

        with open(filepath, 'a', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


    def delete_vacancy(self, vacancy):
        pass


