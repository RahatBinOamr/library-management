# Generated by Django 4.2.6 on 2024-01-11 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='borrowing_book',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]