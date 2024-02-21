from django.http import HttpResponse
from django.shortcuts import render

def index(request): # HttpRequest
    return HttpResponse('Страница приложения women.') # Возврат страницы с надписю про women

def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям </h1><p>id: {cat_id}</p>') # Возврат страницы с надписю про categories

def categories_by_slug(request, cat_slug): # добавляем возможность вводить не только int, но и любые символы
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')


