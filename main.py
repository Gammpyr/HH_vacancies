from src.file_workers import JSONSaver
from src.parser import HeadHunterAPI
from src.vacancy import Vacancy

hh_api = HeadHunterAPI()


# Функция для взаимодействия с пользователем
def user_interaction() -> None:
    search_query = input("Введите поисковый запрос: ")
    print("Введите диапазон зарплат: ")
    salary_from = int(input("От: "))
    salary_to = input("До: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(search_query)

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    # Фильтруем по зарплате в указанном диапазоне
    ranged_vacancies = Vacancy.get_vacancies_by_salary(vacancies_list, salary_from, salary_to)

    # Сортируем вакансии по убыванию зарплаты
    sorted_vacancies = Vacancy.sort_vacancies(ranged_vacancies)

    # Отбираем только топ-n вакансий по зарплате
    top_vacancies = Vacancy.get_top_vacancies(sorted_vacancies, top_n)

    # Выводим результат
    Vacancy.print_vacancies(top_vacancies)

    # Узнаём, нужно ли сохранение
    is_save = input("\nСохранить результат в файл? (Да/Нет) -> ")

    # Сохраняем, если пользователь согласился
    if is_save.lower() == "да" or is_save.lower() == "lf":
        filename = input("Введите название для файла -> ")
        json_saver = JSONSaver()
        json_saver.add_vacancy(top_vacancies, filename)
        print(f"Список вакансий сохранён в файл /data/{filename}!")


if __name__ == "__main__":
    user_interaction()
