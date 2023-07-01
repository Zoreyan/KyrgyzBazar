import django_filters
from .models import *

class VacancyFilter(django_filters.FilterSet):
    class Meta:
        model = Vacancy
        fields = ['title', 'city']