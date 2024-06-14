from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=300)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    footage = models.PositiveSmallIntegerField(blank=True, null=True, help_text="nekdy...")
    description = models.TextField(blank=True)
    main_picture = models.CharField(blank=True, default="", max_length = 2000)
    director = models.ForeignKey('Director', blank=True, null=True, on_delete=models.SET_NULL)
    actors = models.ManyToManyField('Actor', blank=True, null=True)
    genres = models.ManyToManyField('Genre', blank=True, null=True) 

    def __str__(self):
        return self.name
    
    def genres_display(self):
        return ",".join([i.name for i in self.genres.all()])

class Director(models.Model):
    name = models.CharField(max_length=300)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    main_picture = models.CharField(blank=True, default="", max_length = 2000)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=30)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    main_picture = models.CharField(blank=True, default="", max_length = 2000)
    
    def __str__(self):
        return self.name
    

class Genre(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
