# Generated by Django 4.2.6 on 2024-01-11 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(default='default.png', upload_to='author')),
                ('occupation', models.CharField(max_length=255)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='default.png', upload_to='category')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='availability_status',
            field=models.CharField(blank=True, choices=[('available', 'available'), ('not available', 'not available'), ('coming soon', 'coming soon')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='book.category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='book.author'),
        ),
    ]