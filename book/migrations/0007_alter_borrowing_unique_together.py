# Generated by Django 5.0.1 on 2024-01-12 16:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_rename_product_description_book_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='borrowing',
            unique_together={('user', 'book')},
        ),
    ]
