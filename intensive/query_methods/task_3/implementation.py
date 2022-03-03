from collections import defaultdict

from django.db.models import Sum, F, OuterRef, Subquery

from ..models import *


def get_top_order_by_sum_in_period(begin, end):
    """Возвращает заказ, который имеют наибольшую сумму за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает номер заказа и его сумму
    """

    qs = OrderItem.objects.filter(
        order__date_formation__gte=begin,
        order__date_formation__lte=end
    ).order_by('-order').select_related('product', 'order')
    orders_sum = {}
    for item in qs:
        product_cost = item.product.productcost_set.filter(
            begin__lte=item.order.date_formation, end__gte=item.order.date_formation).first()
        cost = product_cost.value if product_cost else 0
        if orders_sum.get((item.order_id, item.order.number)):
            orders_sum[(item.order_id, item.order.number)] += cost * item.count
        else:
            orders_sum[(item.order_id, item.order.number)] = cost * item.count
    lst = [[key[0], key[1], item] for key, item in orders_sum.items()]
    lst.sort(key=lambda x: x[1], reverse=True)
    lst.sort(key=lambda x: x[2], reverse=True)

    return (lst[0][1], lst[0][2]) if lst else None
