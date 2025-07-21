function printSongs(arrayOfSongs) {
    let numOfSongs = arrayOfSongs.shift();
    let typeOfSong = arrayOfSongs.pop();

    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }

    let songs = [];

    arrayOfSongs.forEach(element => {
        let [typeList, name, time] = element.split("_");
        let song = new Song(typeList, name, time);
        songs.push(song);
    });

    if (typeOfSong === "all") {
        songs.forEach(song => console.log(song.name));
    } else {
        songs
            .filter(song => song.typeList === typeOfSong)
            .forEach(song => console.log(song.name));
    }
}
