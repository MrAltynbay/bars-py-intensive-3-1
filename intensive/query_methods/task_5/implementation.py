from decimal import Decimal
from statistics import mean

from django.db.models import Avg, F

from ..models import *


def get_average_cost_without_product(product, begin, end):
    """Возвращает среднюю стоимость заказов без указанного товара за определенный промежуток времени

    Args:
        product: наименование товара
        begin: начало периода
        end: окончание периода

    Returns: возвращает числовое значение средней стоимости
    """
    # !!!Не работает!!!
    # qs = OrderItem.objects.filter(
    #     order__date_formation__gte=begin,
    #     order__date_formation__lte=end
    # ).exclude(product__name=product).select_related('product', 'order')
    # orders_sum = {}
    # for item in qs:
    #     product_cost = item.product.productcost_set.filter(
    #         begin__lte=item.order.date_formation, end__gte=item.order.date_formation).first()
    #     cost = product_cost.value if product_cost else 0
    #     if orders_sum.get((item.order_id, item.order.number)):
    #         orders_sum[(item.order_id, item.order.number)] += cost * item.count
    #     else:
    #         orders_sum[(item.order_id, item.order.number)] = cost * item.count
    # lst = [[key[0], key[1], item] for key, item in orders_sum.items()]
    # orders_lst = []
    #
    # for items in lst:
    #     for itemm in items:
    #         orders_lst.append(itemm)
    # price_lst = orders_lst[2::3]
    # for i in price_lst:
    #     if int(i) == 0:
    #         price_lst.remove(i)
    # if price_lst:
    #     return mean(price_lst)
    # else:
    #     Decimal(0)
