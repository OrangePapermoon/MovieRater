# MovieRater

A Django web app for browsing movies, built on [The Movie Database (TMDB) API](https://developer.themoviedb.org/). Users can create an account, browse top-rated movies, search by title with infinite scroll, and open a detail page for any movie.

I built this project while learning web development through Harvard's *CS50's Web Programming with Python and JavaScript*.

> **Status:** work in progress. Browsing, search and accounts work; rating and reviewing movies (the app's namesake feature) is not built yet. See [Roadmap](#roadmap).

<!-- Screenshots: add 2–3 images here, e.g. the home page, search results and a movie page -->
<!-- ![Home page](docs/home.png) -->

## Features

- **Top-rated movies on the home page:** posters and titles pulled live from TMDB
- **Search by title:** results from TMDB's search endpoint
- **Infinite scroll:** more search results load automatically as you scroll, fetched as JSON from a Django endpoint with vanilla JavaScript
- **Movie detail pages:** title, poster, genres, country of origin, release date and overview
- **User accounts:** register, log in and log out using Django's built-in authentication
  - Movie pages and search require login (`@login_required`)
  - Logout uses a POST form with a CSRF token, not a plain link
  - The navbar changes based on login state ("Hi, *username*" / Log out vs. Register / Log in)
- **API keys kept out of code:** credentials load from a `.env` file via `python-dotenv`

## Tech stack

| Layer | Tools |
| --- | --- |
| Backend | Python 3.9, Django 4.2 |
| Data source | TMDB API v3 (called with `requests`) |
| Frontend | Django templates, vanilla JavaScript (Fetch API), Bootstrap 5 (navbar) |
| Database | SQLite (user accounts) |
| Config | `python-dotenv` |

## Getting started

### 1. Get a TMDB token

Create a free account at [themoviedb.org](https://www.themoviedb.org/), then go to **Settings → API** and copy your **API Read Access Token** (the long token, not the short API key). The app sends it as a Bearer token.

### 2. Install

```bash
git clone https://github.com/OrangePapermoon/MovieRater.git
cd MovieRater
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure

Create a `.env` file in the project root (it is already in `.gitignore`):

```
SECRET_KEY=any-long-random-string
TMDB_API_KEY=your-tmdb-api-read-access-token
```

### 4. Run

```bash
python manage.py migrate
python manage.py runserver
```

Open **http://127.0.0.1:8000/movies/** (the app lives under `/movies/`; the site root `/` is not routed).

## How it works

| Page | URL | TMDB endpoint | Login required |
| --- | --- | --- | --- |
| Home (top-rated) | `/movies/` | `GET /3/movie/top_rated` | No |
| Search results | `/movies/search?title=…` | `GET /3/search/movie` | Yes |
| Next page of results (JSON) | `/movies/search_scroll?title=…&page=…` | `GET /3/search/movie` | No |
| Movie details | `/movies/<id>` | `GET /3/movie/{id}` | Yes |
| Register / Log in / Log out | `/accounts/register`, `/accounts/login`, `/accounts/logout` | — | Log out only |

Infinite scroll: `movies/static/movies/js/scroll.js` watches the scroll position. When you reach the bottom of the page, it requests the next page from `/movies/search_scroll`, which proxies TMDB and returns JSON, and then appends the new results to the list. The TMDB token stays on the server.

## Project structure

```
MovieRater/
├── mrater/          # Project settings and root URL config
├── movies/          # Movie browsing: views, URLs, templates, scroll.js
├── accounts/        # Registration, login, logout
├── templates/
│   └── base.html    # Shared layout and auth-aware navbar
└── manage.py
```

## Known issues

- The home page heading says "Top Trending," but the data comes from TMDB's **top-rated** endpoint.
- Search titles are not URL-encoded, so titles containing `&` or `#` can return wrong results.
- `/movies/search_scroll` is not login-protected, unlike the search page.

## Roadmap

- [ ] Rate and review movies (models for ratings and reviews, saved per user)
- [ ] "My ratings" page
- [ ] Better styling with Bootstrap cards and a responsive grid
- [ ] Error handling for failed or slow TMDB requests
- [ ] Tests for views and authentication
- [ ] Deploy a live demo

## Credits

This product uses the TMDB API but is not endorsed or certified by TMDB.
