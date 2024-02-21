from django.http import HttpResponse
from django.shortcuts import render

def index(requset): # HttpRequest
    return HttpResponse('Страница приложения women.') # Возврат страницы с надписю про women

def categories(request):
    return HttpResponse('<h1>Статьи по категориям </h1>') # Возврат страницы с надписю про categories