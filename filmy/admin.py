from django.contrib import admin

from filmy.models import Movie, Director, Genre, Actor


class MovieAdmin(admin.ModelAdmin):
    
    list_display = ["id", "name", "year", "footage", "director", "genres_display", "main_picture"]
    list_display_links = ["id", "name"]
    search_fields = ["=id", "name", "director__name"]
    list_filter = ["year", "genres"]
    list_editable = ["year", "footage", "main_picture"]


class DirectorAdmin(admin.ModelAdmin):
    
    list_display = ["id", "name", "birth_year", "description", "main_picture"]
    list_display_links = ["id", "birth_year"]
    search_fields = ["=id", "name", "birth_year"]
    list_editable = ["name", "description", "main_picture"]


class GenreAdmin(admin.ModelAdmin):
    
    list_display = ["id", "name"]
    list_display_links = ["id"]
    search_fields = ["=id", "name"]
    list_editable = ["name"]


class ActorAdmin(admin.ModelAdmin):
    
    list_display = ["id", "name", "birth_year", "description", "main_picture"]
    list_display_links = ["id", "birth_year"]
    search_fields = ["=id", "name", "birth_year"]
    list_editable = ["name", "description",  "main_picture"]


admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Actor, ActorAdmin)

# Register your models here.
