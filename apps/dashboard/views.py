from django.shortcuts import render, redirect
from .models import *
from apps.store.models import *
from apps.blog.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from .filter import *

class ChangePasswordView(PasswordChangeView):
    form_class = MyPasswordChangeForm
    template_name = "dashboard/forms/password_form.html"

# List
@login_required(login_url='login')
def dashboard_view(request):
    vacancies = Vacancy.objects.filter(owner=request.user).order_by('-id')[:5]
    orders = Order.objects.filter(owner=request.user).order_by('-id')[:5]
    reports = Report.objects.filter(owner=request.user).order_by('-id')[:5]
    pictures = Pictures.objects.filter(owner=request.user).order_by('-id')[:4]
    todos = Todo.objects.filter(owner = request.user)
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
    if request.method == 'POST' and 'delete' in request.POST:
        todo_id = request.POST.get('delete')
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
    
    context = {
        'vacancies': vacancies,
        'reports': reports,
        'orders': orders,
        'pictures': pictures,
        'todos': todos,
        'form': form,
    }
    return render(request, 'dashboard/main.html', context)

@login_required(login_url='login')
def todo_list_view(request):
    todos = Todo.objects.filter(owner = request.user)
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
            return redirect('todo-list')
    if request.method == 'POST' and 'delete' in request.POST:
        todo_id = request.POST.get('delete')
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect('todo-list')
    context = {
        'todos': todos,
        'form': form
    }
    return render(request, 'dashboard/todo_list.html', context)

@login_required(login_url='login')
def report_list_view(request):
    reports = Report.objects.filter(owner = request.user).order_by('-id')
    context = {
        'reports': reports
    }
    return render(request, 'dashboard/report_list.html', context)

def vacancy_list_view(request):
    vacancies = Vacancy.objects.all()
    myFilter = VacancyFilter(request.GET, queryset=vacancies)
    if myFilter:
        vacancies = myFilter.qs
    else:
        vacancies = Vacancy.objects.all()
    context = {
        'vacancies': vacancies,
        'myFilter': myFilter
    }
    return render(request, 'dashboard/vacancy_list.html', context)

@login_required(login_url='login')
def order_list_view(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'dashboard/order_list.html', context)

# Create
@login_required(login_url='login')
def shop_form_view(request):
    cities = City.objects.all()
    categories = ShopCategory.objects.all()
    form = ShopForm()
    if request.method == 'POST':
        city_id =  request.POST.get('city')
        city = City.objects.get(id=city_id)
        type_id =  request.POST.get('type')
        category_id =  request.POST.get('category')
        category = ShopCategory.objects.get(id=category_id)
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.instance.city = city
            form.instance.category = category
            form.instance.type = type_id
            form.save()
            return redirect('shop-list')
    context = {
        'cities': cities,
        'form': form,
        'categories': categories
    }
    return render(request, 'dashboard/forms/shop_form.html', context)

@login_required(login_url='login')
def order_form_view(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return redirect('order-list')
    context = {
        'form': form,
    }
    return render(request, 'dashboard/forms/order_form.html', context)

@login_required(login_url='login')
def post_form_view(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return redirect('post-list')
    context = {
        'form': form,
    }
    return render(request, 'dashboard/forms/post_form.html', context)

@login_required(login_url='login')
def product_form_view(request):
    categories = ProductCustomCategory.objects.filter(owner=request.user)
    shops = Shop.objects.filter(owner=request.user)
    form = ProductForm()
    if request.method == 'POST':
        shop_id =  request.POST.get('shop')
        shop = Shop.objects.get(id=shop_id)
        category_id =  request.POST.get('category')
        category = ProductCustomCategory.objects.get(id=category_id)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.shop = shop
            form.instance.category = category
            form.instance.owner = request.user
            form.save()
            return redirect('dashboard-main')
    context = {
        'categories': categories,
        'form': form,
        'shops': shops
    }
    return render(request, 'dashboard/forms/product_form.html', context)

@login_required(login_url='login')
def report_form_view(request):
    form = ReportForm()
    if request.method == 'POST':
        description_id =  request.POST.get('description')
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.instance.description = description_id
            form.save()
            return redirect('report-list')
    context = {
        'form': form,
    }
    return render(request, 'dashboard/forms/report_form.html', context)

@login_required(login_url='login')
def vacancy_form_view(request):
    cities = City.objects.all()
    shops = Shop.objects.filter(owner=request.user)
    form = VacancyForm()
    if request.method == 'POST':
        city_id =  request.POST.get('city')
        city = City.objects.get(id=city_id)
        shop_id =  request.POST.get('shop')
        shop =  Shop.objects.get(id=shop_id)
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form.instance.city = city
            form.instance.shop = shop
            form.save()
            return redirect('vacancy-list')
    context = {
        'cities': cities,
        'shops': shops,
        'form': form,
    }
    return render(request, 'dashboard/forms/vacancy_form.html', context)

@login_required(login_url='login')
def category_form_view(request):
    shops = Shop.objects.filter(owner=request.user)
    form = ProductCustomCategoryForm()
    if request.method == 'POST':
        shop_id =  request.POST.get('shop')
        shop = Shop.objects.get(id=shop_id)
        form = ProductCustomCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.shop = shop
            form.instance.owner = request.user
            form.save()
            return redirect('dashboard-main')
    context = {
        'form': form,
        'shops': shops
    }
    return render(request, 'dashboard/forms/category_form.html', context)

def image_form_view(request):
    shops = Shop.objects.filter(owner=request.user)
    form = ImageForm()
    if request.method == 'POST':
        shop_id =  request.POST.get('shop')
        shop = Shop.objects.get(id=shop_id)
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.shop = shop
            form.instance.owner = request.user
            form.save()
            return redirect('dashboard-main')
    context = {
        'form': form,
        'shops': shops
    }
    return render(request, 'dashboard/forms/image_form.html', context)


@login_required(login_url='login')
def user_form_view(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.instance.status = request.POST.get('status')
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'dashboard/forms/user_form.html', {'form': form})