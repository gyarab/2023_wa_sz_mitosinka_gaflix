# Generated by Django 5.0.3 on 2024-05-24 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0002_director_genre_rename_title_movie_name_movie_footage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={},
        ),
        migrations.AlterModelOptions(
            name='director',
            options={},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={},
        ),
        migrations.AddField(
            model_name='actor',
            name='birth_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='main_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='director',
            name='main_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='main_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='footage',
            field=models.PositiveSmallIntegerField(blank=True, help_text='in minutes', null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
