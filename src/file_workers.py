import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from src.vacancy import Vacancy


class FileWorker(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def save_to_file(self, data: dict, filename: str) -> None:
        pass

    @abstractmethod
    def get_data_from_file(self) -> None:
        pass


class JSONSaver(FileWorker):
    """Класс для работы с JSON-файлами"""

    def __init__(self) -> None:
        self.datapath = Path("./data/")

    def save_to_file(self, data: dict, filename: str = "hh") -> None:
        """Сохраняет данные в указанный файл"""
        filepath = self.datapath / Path(f"{filename}.json")

        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def get_data_from_file(self, filename: str = "hh") -> Any:
        """Получает данные из указанного файла"""
        filepath = self.datapath / Path(f"{filename}.json")

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

        return data

    def add_vacancy(self, data: list | dict, filename: str = "hh") -> None:
        """Добавляет новую вакансию в указанный файл"""
        filepath = self.datapath / Path(f"{filename}.json")

        json_data = self.get_data_from_file(filename)

        data = Vacancy.cast_to_object_dict(data)
        data = Vacancy.get_unique_vacancy(json_data, data)

        if isinstance(data, dict):
            json_data.append(data)
        else:
            json_data.extend(data)

        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self, filename: str) -> None:
        """Удаляет все данные из указанного файла"""
        filepath = self.datapath / Path(f"{filename}.json")
        try:
            with open(filepath, "w"):
                pass
        except FileNotFoundError:
            print("Такого файла не существует")
