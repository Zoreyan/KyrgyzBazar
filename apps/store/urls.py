from django.urls import path
from .views import *
from .models import *
from apps.users.views import *

urlpatterns =[
    path('profile/<int:pk>/', user_profile, name='user-profile'),# Профиль пользователя
    path('register/', user_register, name='register'),# Регистрация
    path('login/', user_login, name='login'),# Авторизация 
    path('logout/', user_logout, name='logout'),# Выход
    path('', shop_list_view, name='shop-list'),#Отслеживание маршрута на главную страницу
    path('shop-detail/<int:pk>/', shop_detail_view, name='shop-detail'),#Отслеживание маршрута на детальную страницу аниме
    path('product-list', product_list_view, name='product-list'),#Отслеживание маршрута на продуктовую страницу
]