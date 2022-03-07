from django.db import models
from django.db.models import CASCADE, PROTECT


class Recipe(models.Model):
    """
    Модель рецепта
    """

    title = models.CharField('Название', max_length=512)
    description = models.TextField('Описание')

    class Meta:
        db_table = 'recipes_recipe'
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Product(models.Model):
    """
    Модель продукта
    """

    title = models.CharField('Название', max_length=512)
    description = models.TextField('Описание', max_length=2048)

    class Meta:
        db_table = 'products_product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class CookStep(models.Model):
    """
    Шаг приготовления блюда
    """

    title = models.CharField('Название', max_length=512)
    description = models.TextField('Описание')

    recipe = models.ForeignKey(Recipe, on_delete=CASCADE)

    class Meta:
        db_table = 'recipes_cook_step'
        verbose_name = 'Шаг приготовления блюда'
        verbose_name_plural = 'Шаги приготовления блюд'


class RecipeProduct(models.Model):
    """
    Продукт используемый в рецепте
    """

    recipe = models.ForeignKey(Recipe, verbose_name='Рецепт', on_delete=CASCADE)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=PROTECT)

    count = models.DecimalField('Количество', decimal_places=2, max_digits=6)

    class Meta:
        db_table = 'recipes_recipe_product'
        verbose_name = 'Продукт используемый в рецепте'
        verbose_name_plural = 'Продукты используемые в рецепте'

