from django.shortcuts import render

from filmy.models import Movie, Actor, Director

def index(request):
    
    return render(request, 'filmy/base.html')

def movies(request):

    context = {
        'movies': Movie.objects.all().order_by('name')
    }

    return render(request, 'filmy/movies.html', context)

def movie(request, id):
    
    context = {
        'movie': Movie.objects.get(id=id)
    }

    return render(request, 'filmy/movie.html', context)

def actors(request):

    context = {
        'actors': Actor.objects.all().order_by('name')
    }

    return render(request, 'filmy/actors.html', context)

def actor(request, id):
    
    context = {
        'actor': Actor.objects.get(id=id)
    }

    return render(request, 'filmy/actor.html', context)


def directors(request):

    context = {
        'directors': Director.objects.all().order_by('name')
    }

    return render(request, 'filmy/directors.html', context)

def director(request, id):
    
    context = {
        'director': Director.objects.get(id=id)
    }

    return render(request, 'filmy/director.html', context)