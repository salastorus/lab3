import requests
#https://api.vk.com/method/


class BaseClient:
    # URL vk api
    BASE_URL = "https://api.vk.com/method/"
    # метод vk api
    method = None
    # GET, POST, ...
    http_method = None


    # Получение GET параметров запроса
    def get_params(self):
        return None


    # Получение данных POST запроса
    def get_json(self):
        return None


    # Получение HTTP заголовков
    def get_headers(self):
        return None

    # Склейка url printf("%s %d", str, num)
    def generate_url(self, method):
        return '{0}{1}'.format(self.BASE_URL, method)

    # Отправка запроса к VK API
    def _get_data(self, method, http_method):
        resp = requests.get(url=self.generate_url(self.method), params=self.get_params())
        return self.response_handler(resp.json())

    # Обработка ответа от VK API
    def response_handler(self, response):
        return response

    # Запуск клиента
    def execute(self):
        return self._get_data(
            method=self.method,
            http_method=self.http_method
        )