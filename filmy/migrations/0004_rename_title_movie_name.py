# Generated by Django 5.0.3 on 2024-05-17 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0003_director_genre_movie_description_movie_main_picture_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='title',
            new_name='name',
        ),
    ]
