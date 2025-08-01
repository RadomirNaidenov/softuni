function storeInfo(array) {
    let movies = [];

    for (let command of array) {
        if (command.startsWith("addMovie ")) {
            let name = command.replace("addMovie ", "");
            movies.push({ name })

        } else if (command.includes(" directedBy ")) {
            let [name, director] = command.split(" directedBy ");
            let movie = movies.find(m => m.name === name);
            if (movie) {
                movie.director = director
            }

        } else if (command.includes(" onDate ")) {
            let [name, date] = command.split(" onDate ");
            let movie = movies.find(m => m.name === name);
            if (movie) {
                movie.date = date;
            }
        }
    }

    movies
        .filter(m => m.name && m.director && m.date)
        .forEach(m => console.log(JSON.stringify(m)));

}