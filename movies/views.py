from django.shortcuts import render, redirect
from .models import Movie

def home_page(request):
    user_query = str(request.GET.get('query', ''))
    search_result = Movie.objects.filter(name__icontains=user_query)
    stuff_for_frontend = {'search_result': search_result}
    return render(request, 'movies/movies_stuff.html', stuff_for_frontend)

def create(request):
    if request.method == 'POST':
        try:
            response = Movie.objects.create(
                name=request.POST.get('name'),
                picture=request.POST.get('picture'),
                rating=int(request.POST.get('rating')),
                notes=request.POST.get('notes')
            )
        except Exception as e:
            print(e)

    return redirect('/')

def edit(request,movie_id):
    if request.method == 'POST':
        try:
            movie= Movie.objects.get(id=movie_id)
            movie.name = request.POST.get('name')
            movie.picture = request.POST.get('picture')
            movie.rating = int(request.POST.get('rating'))
            movie.notes = request.POST.get('notes')
            movie.save()

        except Exception as e:
            print(e)
        return redirect('/')
