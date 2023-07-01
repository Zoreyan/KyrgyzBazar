from django.urls import path
from .views import *


urlpatterns = [
    path('post-list/', post_list_view, name='post-list'),
    path('post-detail/<int:pk>/', post_detail_view, name='post-detail'),
]