from random import choice
from string import ascii_letters

import psycopg2
from django.db import OperationalError
from django.shortcuts import render
from django.views import View

from workers.models import Worker


class Task1View(View):
    """
    Страничка при открытии которой автоматически создает несколько записей Worker
    """

    def get(self, request, **kwargs):
        a_random_name = ''.join(choice(ascii_letters) for i in range(6))
        b_random_name = ''.join(choice(ascii_letters) for i in range(6))
        a = Worker(name=a_random_name)
        b = Worker(name=b_random_name)
        a.save()
        b.save()
        workers = Worker.objects.values_list('id', 'name')

        return render(
            request=request,
            template_name='task.html',
            context={'workers': list(workers)},
        )


class Task2View(View):
    """
    Страничка c отображением списка Worker из основного сервера
    """

    def get(self, request, **kwargs):
        workers = Worker.objects.values_list('id', 'name')

        return render(
            request=request,
            template_name='task.html',
            context={'workers': list(workers)},
        )


class Task3View(View):
    """
        Страничка c отображением списка Worker из реплики
    """

    def get(self, request, **kwargs):
        workers = Worker.from_replica.values_list('id', 'name')

        return render(
            request=request,
            template_name='task.html',
            context={'workers': list(workers)},
        )


class Task4View(View):
    """
    Дополнительно создать страницу со отображением Worker’s из реплики если основной сервер не работает
    """

    def get(self, request, **kwargs):
        try:
            conn = psycopg2.connect("dbname='default' user='postgres' host='127.0.0.1' password='salavat1337' connect_timeout=1 ")
            conn.close()
            is_connected = True

        except:
            is_connected = False

        if is_connected:
            workers = Worker.objects.values_list('id', 'name')
        else:
            workers = Worker.from_replica.values_list('id', 'name')

        return render(
            request=request,
            template_name='task.html',
            context={'workers': list(workers)},
        )




