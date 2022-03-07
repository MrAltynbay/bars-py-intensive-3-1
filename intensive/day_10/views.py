from django.http import JsonResponse
from django.views import View

from day_10.models import CookStep, RecipeProduct


def calc(request):
    """
    Представление которому в параметре запроса maths через разделитель перечисляются простейшие арифметические операции
    например maths=3*3,10-2,10/5
    по умолчанию в качестве символа разделителя выступает сивол запятой.
    В необязательном параметре delimiter указывается символ разделителя арифметических операций
    например calc/?maths=3*3;10-2;10/5&delimiter=;

    Результат:  JsonResponse вида {'3*3': 9, '10-2': 8, '10/5': 2}
    """
    if request.method == 'GET':
        result = {}
        if 'delimiter' in request.GET:
            delimiter = request.GET['delimiter']
        else:
            delimiter = ','
        if 'maths' in request.GET:
            math_get = request.GET['maths']
            for i in math_get.split(delimiter):
                result[i] = eval(i)

        return JsonResponse(result)


class Task2View(View):
    """
    Вывести детальную информацию рецепта с идентификатором 1.
    Нужно получить информацию о шагах приготовления, списке необходимых продуктов для приготовления
    Шаги представляют собой список:
        - Название шага;
        - Описание шага.
    Продукты представляют собой список:
        - Название продукта;
        - Описание продукта;
        - Количество продукта;
    """

    def get(self, request, **kwargs):
        recipe_id = 1
        steps = list(
            CookStep.objects.filter(
                recipe_id=recipe_id
            ).values_list('title', 'description')
        )
        products = list(
            RecipeProduct.objects.filter(
                recipe_id=recipe_id
            ).values_list('product__title', 'product__description', 'count')

        )

        recipe_data = {
            'steps': steps,
            'products': products,
        }

        # Если есть необходимость посмотреть на выполняемые запросы, план запросов через браузер, то нужно
        # раскомментировать строки ниже
        # return render(
        #     request=request,
        #     template_name='task.html',
        #     context={'json_data': json.dumps(dict(recipe_data=recipe_data), ensure_ascii=False, default=str)},
        # )

        # В тестах проверяется формируемый JSON, поэтому нужно возвращать JsonResponse
        return JsonResponse(dict(recipe_data=recipe_data), json_dumps_params=dict(ensure_ascii=False, default=str))

