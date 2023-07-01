from django.db import models
from apps.users.models import User

class ShopCategory(models.Model):
    title = models.CharField(max_length=40, verbose_name='Название')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории для магазина'

# City
class City(models.Model):
    title = models.CharField(max_length=90, verbose_name='Город')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

# Shop
class Shop(models.Model):
    banner = models.ImageField(upload_to='banners/', null=True, blank=True)
    title = models.CharField(max_length=90, verbose_name='Название')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Владелец')
    category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE, null=True, blank=True)
    TYPE = (
        ('1', 'Магазин'),
        ('2', 'Производитель'),
    )
    image = models.ImageField(upload_to='shop_images/', verbose_name='Фотография магазина')
    description = models.TextField(verbose_name='Описание')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Город')
    street = models.CharField(max_length=34, default='', null=True, verbose_name='Улица')
    type = models.CharField(max_length=20, choices=TYPE, verbose_name='Тип', default=2)
    open_time = models.CharField(max_length=14, default='08:00', null=True, verbose_name='Время открытия')
    close_time = models.CharField(max_length=14, default='21:00', null=True, verbose_name='Время закрытия')
    products_for_credit = models.BooleanField(default=False)
    official_website = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

# Pictures
class Pictures(models.Model):
    image = models.ImageField(upload_to='pictures/', null=True, blank=True, verbose_name='Картинка')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, verbose_name='Магазин', related_name='pictures')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    def __str__(self):
        return self.shop.title
    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    
class ProductCustomCategory(models.Model):
    title = models.CharField(max_length=40, verbose_name='Название')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='custom_category')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории для Товара'

# Products
class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, verbose_name='Магазин', related_name='products')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', related_name='user', blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', verbose_name='Картинка')
    title = models.CharField(max_length=100, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    category = models.ForeignKey(ProductCustomCategory, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'