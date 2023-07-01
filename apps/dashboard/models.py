from django.db import models
from apps.users.models import User
from apps.store.models import Shop
from apps.store.models import City

class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.CharField(max_length=120, verbose_name='Название')
    completed = models.BooleanField(default=False, verbose_name='Завершено')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner.username} - {self.text}'
    

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Report(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.CharField(max_length=40, verbose_name='Действие', null=True, blank=True)
    VALUES = (
        ('1', 'Расход'),
        ('2', 'Прибыль')
    )
    description = models.CharField(max_length=40, choices=VALUES, default=2, verbose_name='Описание')
    amount = models.IntegerField(verbose_name='На сумму')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner.username} - {self.description}'
    

    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'
    

class Vacancy(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=20, verbose_name='Название', null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Магазин')
    description = models.TextField(verbose_name='Описание')
    payment = models.IntegerField(verbose_name='Зарплата')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.owner.username} - {self.shop.title}'
    

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
    

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True)
    product_name = models.CharField(max_length=42, verbose_name='Наименование товара', null=True)
    consumer = models.CharField(max_length=50, verbose_name='Заказчик', null=True)
    count = models.IntegerField(verbose_name='Количество', null=True)
    amount = models.IntegerField(verbose_name='Стоимость товара', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.owner.username} - {self.consumer}'
    
    @property
    def get_amount_total(self):
        total = self.count * self.amount
        return total

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'