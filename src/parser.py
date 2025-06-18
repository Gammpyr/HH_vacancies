from abc import ABC, abstractmethod

import requests


class Parser(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass



class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    def get_vacancies(self, keyword):
        ## сбросить счётчик страниц на 0?
        self.__params['text'] = keyword

        while self.__params.get('page') != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code != 200:
                raise requests.RequestException

            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1

        return self.__vacancies

    # def save_to_file(self, filename='hh'):
    #     filepath = Path('./data/') / Path(f'{filename}.json')
    #     with open(filepath, 'w', encoding='utf-8') as file:
    #         json.dump(self.vacancies, file, indent=4, ensure_ascii=False)




if __name__ == '__main__':
    hh1 = HeadHunterAPI()
    hh1.get_vacancies('python')
    hh1.save_to_file('python_test1')

    # save_to_json = JSONSaver()
    # save_to_json.save_to_file(hh1.vacancies, 'python_test2')
