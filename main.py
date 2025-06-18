# Создание экземпляра класса для работы с API сайтов с вакансиями
from pprint import pprint

from src.parser import HeadHunterAPI
from src.file_workers import JSONSaver
from src.vacancy import Vacancy

# hh_api = HeadHunterAPI()
#
# # Получение вакансий с hh.ru в формате JSON
# hh_vacancies = hh_api.get_vacancies("Python")
#
# # Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

# json_saver = JSONSaver()
# json_saver.save_to_file(hh_vacancies)
#
# # Пример работы конструктора класса с одной вакансией
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/1234>", 100_000,
#                   "Требования: опыт работы от 3 лет...")
#
# vacancy2 = Vacancy("Python Developer2", "<https://hh.ru/vacancy/1234>", 150_000,
#                   "Требования: опыт работы от 5 лет...")

#
# # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.delete_vacancy(vacancy)

# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    filtered_vacancies = Vacancy.filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = Vacancy.get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = Vacancy.sort_vacancies(ranged_vacancies)
    top_vacancies = Vacancy.get_top_vacancies(sorted_vacancies, top_n)
    Vacancy.print_vacancies(top_vacancies)
#
# if __name__ == "__main__":
#     user_interaction()


# if __name__=='__main__':
#
#     json_saver = JSONSaver()
#     json_saver.add_vacancy(vacancy)
#     json_saver.add_vacancy(vacancy2)