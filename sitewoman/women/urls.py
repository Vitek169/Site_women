"""Создаем файл ursl в папке womans, для независимости приложения womans"""
from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")


urlpatterns = [
    path('', views.index, name='home'), # изменяем главную страницу http://127.0.0.1:8000 с выводом статьи 'Страница приложения women.' из views
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('category/<int:cat_id>/', views.show_cantegory, name='category')

]




