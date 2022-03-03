from django.db.models import Sum, Max, IntegerField

from ..models import *


def get_top_product_by_total_count_in_period(begin, end):
    """Возвращает товар, купленный в наибольшем объеме за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает наименование товара и объем
    """

    qs = OrderItem.objects.filter(
        order__date_formation__gte=begin,
        order__date_formation__lte=end
    ).values('product_id').annotate(
        count_sum=Sum('count', output_field=IntegerField())
    ).order_by('-count_sum').values('product__name', 'count_sum').first()
    if qs:
        return [(qs['product__name'], qs['count_sum'])]
    else:
        return []
