# Generated by Django 4.0.2 on 2022-02-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0005_alter_genre_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Жанр'),
        ),
    ]
