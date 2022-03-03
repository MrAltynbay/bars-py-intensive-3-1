from django.db.models import Count, Min

from ..models import *


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """
    qs = Order.objects.filter(
        date_formation__gte=begin, date_formation__lte=end
    ).values(
        'customer_id'
    ).annotate(
        ccount=Count('id'), min_data=Min('date_formation')
    ).order_by(
        '-ccount', 'min_data', 'customer__name'
    ).values_list('customer__name', 'ccount').first()

    return qs
