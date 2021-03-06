# Generated by Django 3.2.8 on 2022-05-26 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20190901_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='book.author', verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.publishing', verbose_name='出版社'),
        ),
    ]
