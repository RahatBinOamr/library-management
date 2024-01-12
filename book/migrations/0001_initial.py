# Generated by Django 4.2.6 on 2024-01-11 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('publication_date', models.DateField()),
                ('genre', models.CharField(max_length=50)),
                ('availability_status', models.BooleanField(default=True)),
                ('num_of_books_available', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
