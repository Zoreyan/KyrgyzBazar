from django.urls import path
from .views import *
from .models import *



urlpatterns =[
    path('main/', dashboard_view, name='dashboard-main'),# Панель управления
    # List
    path('todo-list/', todo_list_view, name='todo-list'),# Список задач
    path('report-list/', report_list_view, name='report-list'),# Список отчётов
    path('vacancy-list/', vacancy_list_view, name='vacancy-list'),# Список вакансий
    path('order-list/', order_list_view, name='order-list'),# Список вакансий
    # Create
    path('report-form/', report_form_view, name='report-form'),# Форма отчёта
    path('vacancy-form/', vacancy_form_view, name='vacancy-form'),# Форма вакансии
    path('order-form/', order_form_view, name='order-form'),# Форма заказа
    path('shop-form/', shop_form_view, name='shop-form'),# Форма магазина
    path('product-form/', product_form_view, name='product-form'),# Форма товара
    path('category-form/', category_form_view, name='category-form'),# Форма категории
    path('post-form/', post_form_view, name='post-form'),# Форма поста
    path('image-form/', image_form_view, name='image-form'),# Форма изображения
    path('user-form/', user_form_view, name='user-form'),# Форма изображения
    path('password-form/', ChangePasswordView.as_view(
    ), name='password-form'), # Форма пароля
]