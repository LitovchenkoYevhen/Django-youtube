from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


def index(request):
    news = News.objects.order_by('-created_at')
    #categories = Category.objects.all()             Убрали потому, что добавили декоратор в news_tags.py и в _sidebar.html импортировали его и записали её в переменную
    context = {                                    # {% load news_tags %}
        'news': news,                              # {% get_categories as categories %}
        'title': 'Список новостей',
    }
    return render(request, 'news./index.html', context)


def get_category(request, category_pk):
    news = News.objects.filter(category_id=category_pk)
    #categories = Category.objects.all()
    category = Category.objects.get(pk=category_pk)
    context = {'news': news, 'category': category} # удалена 'categories'
    return render(request, 'news/category.html', context)


