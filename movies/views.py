from django.shortcuts import render, redirect
from .models import Movie
from django.contrib import messages


def home_page(request):
    user_query = str(request.GET.get('query', ''))
    search_result = Movie.objects.filter(name__icontains=user_query)
    stuff_for_frontend = {'search_result': search_result}
    return render(request, 'movies/movies_stuff.html', stuff_for_frontend)

def create(request):
    if request.method == 'POST':
        try:
            movie_name = request.POST.get('name')
            response = Movie.objects.create(
                name=request.POST.get('name'),
                picture=request.POST.get('picture'),
                rating=int(request.POST.get('rating')),
                notes=request.POST.get('notes')
            )
            messages.success(request,"New movie added {}".format(movie_name))
        except Exception as e:
            messages.warning(request,"Error while adding a movie {}".format(e))
            print(e)

    return redirect('/')

def edit(request,movie_id):
    if request.method == 'POST':
        try:
            movie_obj= Movie.objects.get(id=movie_id)
            movie_name = request.POST.get('name')
            movie_obj.name = request.POST.get('name')
            movie_obj.picture = request.POST.get('picture')
            movie_obj.rating = int(request.POST.get('rating'))
            movie_obj.notes = request.POST.get('notes')
            movie_obj.save()
            messages.success(request, "movie updated {}".format(movie_name))
        except Exception as e:
            messages.warning(request, f"Error while updating a movie {movie_name}")
    return redirect('/')

def delete(request, movie_id):
    try:

        movie_obj = Movie.objects.get(id=movie_id)
        movie_name = movie_obj.name
        movie_obj.delete()
        messages.success(request, f"deleted Movie {movie_name}")
    except Exception as e:
        messages.warning(request, f"Got error {e} while deleting movie {movie_name}")

    return redirect('/')
