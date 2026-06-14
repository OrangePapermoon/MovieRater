from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import os
import requests
import json

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

@login_required
def movie(request, movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    response = requests.get(url, headers=get_tmdb_headers())
    movie_info = response.json()

    return render(request, "movies/movie.html", {
        "movie": movie_info
    })

@login_required
def search(request):
    movie_list = []

    title = request.GET.get("title", "")
    url = f"https://api.themoviedb.org/3/search/movie?query={title}"

    response = requests.get(url, headers=get_tmdb_headers())
    data = response.json()   
    movie_list = data.get("results", [])

    return render(request, "movies/search.html", {
        "movies": movie_list
    })

def search_scroll(request):
    # get information from fetch
    title = request.GET.get("title", "") # request.GET is essentially a dictionary that Django automatically build from the URL's query string.
    page = request.GET.get("page", 1)

    # fecth data from the api
    url = f"https://api.themoviedb.org/3/search/movie?query={title}&page={page}"

    response = requests.get(url, headers=get_tmdb_headers())
    data = response.json()
    movie_list = data.get("results", [])

    # response to the fetch request
    return JsonResponse({"movies": movie_list})