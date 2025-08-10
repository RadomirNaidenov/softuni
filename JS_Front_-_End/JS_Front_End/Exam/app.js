const loadBtn = document.getElementById('load-movies');
const addBtn = document.getElementById('add-movie');
const editBtn = document.getElementById('edit-movie');

const titleInput = document.getElementById('title');
const directorInput = document.getElementById('director');
const yearInput = document.getElementById('year');

const movieList = document.getElementById('movie-list');

let editingId = null;

loadBtn.addEventListener('click', loadMovies);
addBtn.addEventListener('click', onAddMovie);
editBtn.addEventListener('click', onEditMovie);

// При зареждане Edit Movie бутонът е изключен
editBtn.disabled = true;

async function loadMovies() {
    try {
        const res = await fetch('http://localhost:3030/jsonstore/movies/');
        if (!res.ok) throw new Error('Failed to load movies');

        const data = await res.json();

        // Премахваме всички текущи филми
        while (movieList.firstChild) {
            movieList.removeChild(movieList.firstChild);
        }

        Object.values(data).forEach(movie => {
            const movieDiv = document.createElement('div');
            movieDiv.className = 'movie';

            // Създаваме контейнер за текстовете
            const contentDiv = document.createElement('div');
            contentDiv.className = 'content';

            const pTitle = document.createElement('p');
            pTitle.textContent = movie.title;

            const pDirector = document.createElement('p');
            pDirector.textContent = movie.director;

            const pYear = document.createElement('p');
            pYear.textContent = movie.year;

            contentDiv.appendChild(pTitle);
            contentDiv.appendChild(pDirector);
            contentDiv.appendChild(pYear);

            movieDiv.appendChild(contentDiv);

            // Контейнер за бутоните
            const buttonsDiv = document.createElement('div');
            buttonsDiv.className = 'buttons-container';

            const changeBtn = document.createElement('button');
            changeBtn.className = 'change-btn';
            changeBtn.textContent = 'Edit';
            changeBtn.addEventListener('click', () => startEdit(movie, movieDiv));

            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'delete-btn';
            deleteBtn.textContent = 'Remove';
            deleteBtn.addEventListener('click', () => deleteMovie(movie._id));

            buttonsDiv.appendChild(changeBtn);
            buttonsDiv.appendChild(deleteBtn);

            movieDiv.appendChild(buttonsDiv);

            movieList.appendChild(movieDiv);
        });

        editBtn.disabled = true;
        addBtn.disabled = false;

    } catch (err) {
        alert(err.message);
    }
}

async function onAddMovie(e) {
    e.preventDefault();

    const title = titleInput.value.trim();
    const director = directorInput.value.trim();
    const year = yearInput.value.trim();

    if (!title || !director || !year) {
        alert('All fields are required!');
        return;
    }

    try {
        const res = await fetch('http://localhost:3030/jsonstore/movies/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, director, year }),
        });

        if (!res.ok) {
            const error = await res.json();
            throw new Error(error.message);
        }

        clearForm();
        loadMovies();

    } catch (err) {
        alert(err.message);
    }
}

function startEdit(movie, movieDiv) {
    editingId = movie._id;

    titleInput.value = movie.title;
    directorInput.value = movie.director;
    yearInput.value = movie.year;

    addBtn.disabled = true;
    editBtn.disabled = false;

    // Премахваме филма от DOM-а
    movieList.removeChild(movieDiv);
}

async function onEditMovie(e) {
    e.preventDefault();

    const title = titleInput.value.trim();
    const director = directorInput.value.trim();
    const year = yearInput.value.trim();

    if (!title || !director || !year) {
        alert('All fields are required!');
        return;
    }

    try {
        const res = await fetch(`http://localhost:3030/jsonstore/movies/${editingId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, director, year }),
        });

        if (!res.ok) {
            const error = await res.json();
            throw new Error(error.message);
        }

        clearForm();

        addBtn.disabled = false;
        editBtn.disabled = true;
        editingId = null;

        loadMovies();

    } catch (err) {
        alert(err.message);
    }
}

async function deleteMovie(id) {
    try {
        const res = await fetch(`http://localhost:3030/jsonstore/movies/${id}`, {
            method: 'DELETE',
        });

        if (!res.ok) {
            const error = await res.json();
            throw new Error(error.message);
        }

        loadMovies();

    } catch (err) {
        alert(err.message);
    }
}

function clearForm() {
    titleInput.value = '';
    directorInput.value = '';
    yearInput.value = '';
}