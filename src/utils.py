import json
from pathlib import Path
from typing import Any


def check_salary_type(vacancy1: Any, vacancy2: Any) -> None:
    """Проверка корректности типа при сравнении зарплат в Vacancy"""
    from src.vacancy import Vacancy
    if isinstance(vacancy1, Vacancy) and isinstance(vacancy2, Vacancy):
        return
    else:
        raise TypeError("Можно сравнивать только объекты класса Vacancy")


def is_string(data: Any, text: str) -> None:
    """Проверка, является ли значение строкой"""
    if not isinstance(data, str):
        raise TypeError(f"{text} должно быть строкой")


def is_empty(data, text):
    if not data.strip():
        raise ValueError(f"Строка '{text}' не должна быть пустой")
