from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Category
from news.forms import NewsForm


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

def view_news(request, news_pk):
    # news_item = News.objects.get(pk=news_pk)
    news_item = get_object_or_404(News, pk=news_pk)
    context = {'news_item': news_item}
    return render(request, 'news/view_news.html', context)

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data) # просто показали, что словарь создается, если данные прошли валидацию
            # news = News.objects.create(**form.cleaned_data)  # сохранение данных НЕ НУЖНО В СЛУЧАЕ ФОРМ, СВЯЗАННЫХ С МОДЕЛЯМИ
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
