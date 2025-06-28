function findOccurances(text, wordToSearch) {
    let occurances = 0;

    let textWords = text.split(" ")

    for (const word of textWords) {
        if (word === wordToSearch) {
            occurances += 1;
        }
    }

    console.log(occurances);
    
}