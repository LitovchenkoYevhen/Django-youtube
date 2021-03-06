# Generated by Django 3.2 on 2021-05-11 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210508_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Наименование категории'),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Категория'),
        ),
    ]
