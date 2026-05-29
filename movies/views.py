from django.shortcuts import render

import os
import requests

def get_tmdb_headers():
    token = os.getenv("TMDB_API_KEY")
    return {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

# Create your views here.
def index(request):
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

    response = requests.get(url, headers=get_tmdb_headers())
    data = response.json()
    movie_list = data.get("results", [])

    return render(request, "movies/index.html", {
        "movies": movie_list
    })

def movie(request, movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    response = requests.get(url, headers=get_tmdb_headers())
    movie_info = response.json()

    return render(request, "movies/movie.html", {
        "movie": movie_info
    })

def search(request):
    movie_list = []

    if request.method == "POST":
        title = request.POST.get("title")

        url = f"https://api.themoviedb.org/3/search/movie?query={title}"

        response = requests.get(url, headers=get_tmdb_headers())
        data = response.json()   
        movie_list = data.get("results", [])

    return render(request, "movies/search.html", {
        "movies": movie_list
    })