

document.addEventListener('DOMContentLoaded', function() {
    let page = 1;
    window.onscroll = () => {
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
            page++;
            const title = new URLSearchParams(window.location.search).get('title');

            // // send page and title information to the server and fetch movies of the corresponding page from the server
            fetch(`/movies/search_scroll?title=${title}&page=${page}`)
            .then(response => response.json())
            .then(data => data.movies.forEach(movie => {
                const raw = document.createElement('li');
                if (movie.poster_path) {
                    raw.innerHTML = `
                    <img src="https://image.tmdb.org/t/p/w185/${movie.poster_path}">
                    <p>
                        <a href="/movies/${movie.id}">
                            ${movie.title}
                        </a>
                    </p>
                    `;
                } else {
                    raw.innerHTML = `
                    No poster available
                    <p>
                        <a href="/movies/${movie.id}">
                            ${movie.title}
                        </a>
                    </p>
                    `;
                }

                document.querySelector('ul').append(raw);
            }))
        }
    };
});