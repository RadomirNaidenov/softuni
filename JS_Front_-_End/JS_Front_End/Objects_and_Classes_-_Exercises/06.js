function findWord(array) {
    let obj = {};

    let wordsToFind = array.shift().split(" ");

    for (let word of wordsToFind) {
        obj[word] = 0;
    }

    for (const str of array) {
        if (obj.hasOwnProperty(str)) {
            obj[str] += 1;
        }
    }

    let sorted = Object.entries(obj).sort(([, a], [, b]) => b - a);

    sorted.forEach(([word, count]) => {
        console.log(`${word} - ${count}`);
    });
}
