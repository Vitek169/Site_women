from django import template
import women.views as views

"""Создаем экземпляр класса Library которая будет регистрировать теги"""
register = template.Library()



"""Созздаем функцию которая возвращает список категорий с декоратором register и указываем, что регистрируемый тег будет простым(simple_tag), тем самым мы получаем функцию преобразованную в тег"""
@register.simple_tag(name='getcats')
def get_categories():
    return views.cats_db

@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = views.cats_db
    return {'cats': cats, 'cat_selected': cat_selected}


