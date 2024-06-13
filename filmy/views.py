from django.shortcuts import render
from django.db.models import Q

from filmy.models import Movie
# Create your views here.

def movies(request):
    movies = Movie.objects.all().order_by('name')
    search = request.GET.get('search')
    if search:
        movies = movies.filter(Q(name__icontains=search)|Q(description__icontains=search)) 
    context = {
        'movies': movies,
        "search": search,
    }
    return render (request, 'filmy/movies.html', context)

def movie(request, id):
    context = {
        'movie': Movie.objects.get(id=id)
    }
    return render (request, 'filmy/movie.html', context)