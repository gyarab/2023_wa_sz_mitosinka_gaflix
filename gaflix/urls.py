
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from filmy.views import movies, movie, actor, actors, director, directors

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='filmy/prvni.html'), name='home'),
    path('druha/', TemplateView.as_view(template_name='filmy/druha.html'), name='druha'),
    path('movies/', movies, name="movies"),
    path('movie/<int:id>', movie, name="movie"),
    path('actors/', actors, name="actors"),
    path('actor/<int:id>', actor, name="actor"),
    path('directors/', directors, name="directors"),
    path('director/<int:id>', director, name="director"),
]
