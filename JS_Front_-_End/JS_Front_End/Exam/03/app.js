const host = 'http://localhost:3030/jsonstore/movies';

const movieList = document.getElementById('movie-list');
const loadBtn = document.getElementById('load-movies');
const addBtn = document.getElementById('add-movie');
const editBtn = document.getElementById('edit-movie');

const inputTitle = document.getElementById('title');
const inputDirector = document.getElementById('director');
const inputYear = document.getElementById('year');

let currentEditId = null;

loadBtn.addEventListener('click', loadMovies);
addBtn.addEventListener('click', onAddMovie);
editBtn.addEventListener('click', onEditMovie);

editBtn.disabled = true;

async function loadMovies() {
    movieList.innerHTML = ''; // чисти списъка
    editBtn.disabled = true;
    addBtn.disabled = false;
    currentEditId = null;

    try {
        const res = await fetch(host);
        if (!res.ok) {
            throw new Error('Error loading movies');
        }

        const data = await res.json();

        // data е обект, keys са id-та
        Object.values(data).forEach(movie => {
            const movieDiv = createMovieDiv(movie);
            movieList.appendChild(movieDiv);
        });
    } catch (err) {
        alert(err.message);
    }
}

function createMovieDiv(movie) {
    const divMovie = document.createElement('div');
    divMovie.className = 'movie';

    const divContent = document.createElement('div');
    divContent.className = 'content';

    const pTitle = document.createElement('p');
    pTitle.textContent = movie.title;
    const pDirector = document.createElement('p');
    pDirector.textContent = movie.director;
    const pYear = document.createElement('p');
    pYear.textContent = movie.year;

    divContent.appendChild(pTitle);
    divContent.appendChild(pDirector);
    divContent.appendChild(pYear);

    const btnContainer = document.createElement('div');
    btnContainer.className = 'buttons-container';

    const btnEdit = document.createElement('button');
    btnEdit.className = 'change-btn';
    btnEdit.textContent = 'Edit';
    btnEdit.addEventListener('click', () => onEditClick(movie, divMovie));

    const btnDelete = document.createElement('button');
    btnDelete.className = 'delete-btn';
    btnDelete.textContent = 'Remove';
    btnDelete.addEventListener('click', () => onDeleteClick(movie._id));

    btnContainer.appendChild(btnEdit);
    btnContainer.appendChild(btnDelete);

    divMovie.appendChild(divContent);
    divMovie.appendChild(btnContainer);

    return divMovie;
}

function onEditClick(movie, movieDiv) {
    // премахни филма от списъка (DOM)
    movieList.removeChild(movieDiv);

    // попълни формата
    inputTitle.value = movie.title;
    inputDirector.value = movie.director;
    inputYear.value = movie.year;

    // активирай бутона Edit, деактивирай Add
    editBtn.disabled = false;
    addBtn.disabled = true;

    currentEditId = movie._id;
}

async function onAddMovie() {
    const title = inputTitle.value.trim();
    const director = inputDirector.value.trim();
    const year = inputYear.value.trim();

    if (title === '' || director === '' || year === '') {
        alert('All fields are required!');
        return;
    }

    try {
        const res = await fetch(host, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, director, year }),
        });

        if (!res.ok) {
            throw new Error('Failed to add movie');
        }

        // след добавяне - презареждаме списъка
        await loadMovies();

        // изчистваме формата
        inputTitle.value = '';
        inputDirector.value = '';
        inputYear.value = '';

    } catch (err) {
        alert(err.message);
    }
}

async function onEditMovie() {
    if (!currentEditId) {
        return;
    }

    const title = inputTitle.value.trim();
    const director = inputDirector.value.trim();
    const year = inputYear.value.trim();

    if (title === '' || director === '' || year === '') {
        alert('All fields are required!');
        return;
    }

    try {
        const res = await fetch(`${host}/${currentEditId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, director, year }),
        });

        if (!res.ok) {
            throw new Error('Failed to edit movie');
        }

        await loadMovies();

        inputTitle.value = '';
        inputDirector.value = '';
        inputYear.value = '';

        editBtn.disabled = true;
        addBtn.disabled = false;
        currentEditId = null;
    } catch (err) {
        alert(err.message);
    }
}

async function onDeleteClick(id) {
    try {
        const res = await fetch(`${host}/${id}`, {
            method: 'DELETE',
        });

        if (!res.ok) {
            throw new Error('Failed to delete movie');
        }

        await loadMovies();

    } catch (err) {
        alert(err.message);
    }
}