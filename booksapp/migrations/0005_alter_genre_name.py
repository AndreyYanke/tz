# Generated by Django 4.0.2 on 2022-02-13 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0004_alter_genre_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Жанр'),
        ),
    ]
