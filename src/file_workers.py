import json
from abc import ABC, abstractmethod
from pathlib import Path

from src.vacancy import Vacancy

class FileWorker(ABC):

    @abstractmethod
    def save_to_file(self, data, filename):
        pass

    @abstractmethod
    def get_data_from_file(self):
        pass

class JSONSaver(FileWorker):
    """Класс для сохранения в JSON-файл"""

    def __init__(self):
        self.datapath = Path('./data/')

    def save_to_file(self, data, filename='hh'):
        """Сохраняет данные в указанный файл"""
        filepath = self.datapath / Path(f'{filename}.json')

        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def get_data_from_file(self, filename: str ='hh'):
        """Получает данные из указанного файла"""
        filepath = self.datapath / Path(f'{filename}.json')

        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data


    def add_vacancy(self, data: Vacancy | list[dict], filename: str='hh'):
        """Добавляет новую вакансию в указанный файл"""
        filepath = self.datapath / Path(f'{filename}.json')

        if isinstance(data, Vacancy):
            data = Vacancy.cast_to_object_dict([data])

        with open(filepath, 'a', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


    def delete_vacancy(self, filename: str):
        """Удаляет все данные из указанного файла"""
        filepath = self.datapath / Path(f'{filename}.json')

        with open(filepath, 'w'):
            pass



