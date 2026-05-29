from django.shortcuts import render

import requests

# Create your views here.
def index(request):
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

    headers = {
        "accept": "applicaton/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMzVlYTIyYzZkZTZmMjhmZjQ5MmUxM2I4MWNjODU5NyIsIm5iZiI6MTc3OTk1MjY1Mi40NTEsInN1YiI6IjZhMTdlYzBjNGY5OGFmNmEwMjE1ZDc2YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.3BclRhhnUzPRAV2sGUIg1IyFRw_3iu3qCFrz2Kt2T84"
        }

    response = requests.get(url, headers=headers)
    data = response.json()
    movie_list = data.get("results", [])

    return render(request, "movies/index.html", {
        "movies": movie_list
    })

def movie(request, movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMzVlYTIyYzZkZTZmMjhmZjQ5MmUxM2I4MWNjODU5NyIsIm5iZiI6MTc3OTk1MjY1Mi40NTEsInN1YiI6IjZhMTdlYzBjNGY5OGFmNmEwMjE1ZDc2YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.3BclRhhnUzPRAV2sGUIg1IyFRw_3iu3qCFrz2Kt2T84"
    }

    response = requests.get(url, headers=headers)
    movie_info = response.json()

    return render(request, "movies/movie.html", {
        "movie": movie_info
    })