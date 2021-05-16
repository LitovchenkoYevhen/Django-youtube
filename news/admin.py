from django.contrib import admin
from .models import Category, News, Question, Choice


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at', 'is_published', 'id')
    list_display_links = ('title',  'id')
    search_fields = ('title', 'created_at', 'updated_at', 'is_published', 'id', 'category')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_display_links = ('id', 'category_name')
    search_fields = ('category_name',)



admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question)
admin.site.register(Choice)
