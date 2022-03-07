import json
import time

from django.db import connection
from django.http import HttpResponse
from django.http import JsonResponse

from django.utils.deprecation import (
    MiddlewareMixin,
)

import sys


class StatisticMiddleware:
    """
    Компонент вычисляющий время выполнения запроса на сервере и размер ответа в байтах.
    Отображает значения в консоли приложения
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        end = time.time()
        print(f'Время вычисления запроса {request} {end - start} секунд')
        print(f'Размер ответа - {sys.getsizeof(response.content)} байт')

        return response


class FormatterMiddleware:
    """
    Компонент форматирующий Json ответ в HttpResponse
    {'key': value} => <p>key = value</p>
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if isinstance(response, JsonResponse):
            content = json.loads(response.content)
            data = []
            for key, value in content.items():
                data.append(f'<p>{key} = {value}</p>')
            response = HttpResponse(data)

        return response


class CheckErrorMiddleware(MiddlewareMixin):
    """
        Перехватывает необработанное исключение в представлении и отображает ошибку в виде
        "Ошибка: {exception}"
    """
    @staticmethod
    def process_exception(request, exception):
        return HttpResponse(f'Ошибка: {exception}')


class AllSqlRequests:
    """
        Выводит список всех sql запросов
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        for sqls in connection.queries:
            print(f'{sqls["sql"]} выполнятся за {sqls["time"]} секунд')

        return response


