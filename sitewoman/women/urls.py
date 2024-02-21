"""Создаем файл ursl в папке womans, для независимости приложения womans"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index), # изменяем главную страницу http://127.0.0.1:8000 с выводом статьи 'Страница приложения women.' из views
    path('cats/', views.categories), #добавляет суффикс women к доменному имени http://127.0.0.1:8000/categories

]