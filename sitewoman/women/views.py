from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


def index(request): # HttpRequest
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    return render(request, 'women/index.html')
def about(request):
    return render(request, 'women/about.html')

def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям </h1><p>id: {cat_id}</p>') # Возврат страницы с надписю про categories

def categories_by_slug(request, cat_slug): # добавляем возможность вводить не только int, но и любые символы
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')

def archive(request, year):
    if year > 2024:
        uri = reverse('cats', args=('music',))
        return redirect(uri)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

