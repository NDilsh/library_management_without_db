# Generated by Django 4.2.3 on 2023-07-16 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_manager', '0003_rename_author_book_author_database_remove_book_genre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_storage',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre_storage',
        ),
        migrations.RemoveField(
            model_name='book',
            name='height_storage',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher_storage',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title_storage',
        ),
    ]
