# Generated by Django 5.0.1 on 2024-01-11 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_product_description_book_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
    ]
