# Generated by Django 5.0.6 on 2024-05-30 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0009_genre_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='movies',
        ),
    ]
