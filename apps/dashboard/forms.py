from apps.store.models import *
from apps.blog.models import *
from .models import *
from django import forms
from apps.users.models import User
from django.contrib.auth.forms import PasswordChangeForm


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "form-control"})
 

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['title', 'image', 'banner', 'description', 'street', 'type', 'open_time', 'close_time', 'products_for_credit', 'official_website', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Название',
                'id': 'title',
                'style': 'color: #fff;'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
                'placeholder': 'Изображение',
                'id': 'image',
            }),
            'banner': forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
                'placeholder': 'Баннер',
                'id': 'banner',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Описание',
                'id': 'description',
                'style': 'color: #fff;'
            }),

            'street': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Улица',
                'id': 'street',
                'style': 'color: #fff;'
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Тип',
                'id': 'type',
                'style': 'color: #fff;'
            }),
            'open_time': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Время открытия',
                'id': 'open_time',
                'style': 'color: #fff;'
            }),
            'close_time': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Время закрытия',
                'id': 'close_time',
                'style': 'color: #fff;'
            }),
            'products_for_credit': forms.CheckboxInput(attrs={
                'class': 'form-check-info form-check-input',
                'type': 'checkbox',
                'id': 'products_for_credit',
                'style': 'color: #fff;'
            }),
            'official_website': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Официальный веб-сайт',
                'id': 'official_website',
                'style': 'color: #fff;'
            }),


        }


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'image', 'price']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Название',
                'id': 'title',
                'style': 'color: #fff;'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
                'placeholder': 'Изображение',
                'id': 'image',
            }),

            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Цена',
                'id': 'price',
                'style': 'color: #fff;'
            }),


        }


class ProductCustomCategoryForm(forms.ModelForm):

    class Meta:
        model = ProductCustomCategory
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Название',
                'id': 'title',
                'style': 'color: #fff;'
            }),
        }


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'image', 'text']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'style': 'color: #fff;'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'type': 'text',
                'style': 'color: #fff;'
            }),
            'image':forms.FileInput(attrs={
                'type': 'file',
                'class': 'form-control',
                'style': 'color: #fff;'
            }),
        }
    

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ['text', 'amount', 'description']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'style': 'color: #fff;',
                'placeholder': 'Купили или продали что-то'
            }),

            'amount':forms.TextInput(attrs={
                'type': 'number',
                'class': 'form-control',
                'style': 'color: #fff;'
            }),
        }
    

class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'payment']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'style': 'color: #fff;',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'type': 'text',
                'style': 'color: #fff;',
            }),

            'payment':forms.TextInput(attrs={
                'type': 'number',
                'class': 'form-control',
                'style': 'color: #fff;'
            }),
        }
    

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['consumer', 'product_name', 'amount', 'count']
        widgets = {
            'consumer': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'style': 'color: #fff;',
            }),
            'product_name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'style': 'color: #fff;',
            }),
            'count':forms.TextInput(attrs={
                'type': 'number',
                'class': 'form-control',
                'style': 'color: #fff;'
            }),
            'amount':forms.TextInput(attrs={
                'type': 'number',
                'class': 'form-control',
                'style': 'color: #fff;'
            }),
        }
    

class ImageForm(forms.ModelForm):

    class Meta:
        model = Pictures
        fields = ['image',]
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
                'id': 'image',
                'style': 'color: #fff;'
            }),
        }
    

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'status', 'whatsapp', 'telegram', 'phone']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Имя',
                'id': 'name',
                'style': 'color: #fff;'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
                'placeholder': 'Аватарка',
                'id': 'avatar',
            }),

            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Логин',
                'id': 'username',
                'style': 'color: #fff;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'E-mail',
                'id': 'email',
                'style': 'color: #fff;'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Контактный номер',
                'id': 'phone',
                'style': 'color: #fff;'
            }),
            'whatsapp': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Whatsapp',
                'id': 'whatsapp',
                'style': 'color: #fff;'
            }),
            'telegram': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Telegram',
                'id': 'telegram',
                'style': 'color: #fff;'
            }),
        }
    

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text', 'completed']

        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Введите задачу',
                'id': 'text',
                'style': 'color: #fff;'
            }),
        }