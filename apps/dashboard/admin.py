from django.contrib import admin
from .models import Todo, Report, Vacancy, Order

admin.site.register([Todo, Report, Vacancy, Order])