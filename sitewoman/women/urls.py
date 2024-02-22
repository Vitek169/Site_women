"""Создаем файл ursl в папке womans, для независимости приложения womans"""
from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")


urlpatterns = [
    path('', views.index), # изменяем главную страницу http://127.0.0.1:8000 с выводом статьи 'Страница приложения women.' из views
    path('cats/<int:cat_id>/', views.categories), #добавляет суффикс women к доменному имени http://127.0.0.1:8000/categories
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
    path('archive/<year4:year>/', views.archive, name='archive'),

]




