from django.db import models
from django.contrib.auth.models import AbstractUser

# Users
class User(AbstractUser):
    avatar = models.ImageField(upload_to='profile_images/', null=True, default='https://thumbs.dreamstime.com/b/default-avatar-profile-icon-vector-social-media-user-portrait-176256935.jpg', verbose_name='Аватарка')
    name = models.CharField(max_length=90, verbose_name='Имя')
    STATUS = (
        ('1', 'Владелец'),
        ('2', 'Продавец'),
        ('3', 'Клиент'),
        ('4', 'Администратор'),
        ('5', 'Другое')
    )
    status = models.CharField(max_length=30, null=True, choices=STATUS, blank=True, verbose_name='Должность')
    email = models.EmailField(unique=True, verbose_name='Электронная почта', null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True, verbose_name='Телефонный номер')
    whatsapp = models.CharField(max_length=12, null=True, blank=True, verbose_name='Whatsapp')
    telegram = models.CharField(max_length=100, null=True, blank=True, verbose_name='Telegram')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        try:
            return self.name
        except:
            return f'{self.name} {self.email}'

# Support
class Support(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользоатель')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return f'{self.user.username} {self.text[0:10]}...'
    
    class Meta:
        verbose_name = 'Поддержка'
        verbose_name_plural = 'Поддержка'