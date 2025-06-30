function revealWords(revealWords, text) {
    let wordArr = revealWords.split(', ');

    for (const word of wordArr) {
        let wordTemplate = "*".repeat(word.length);
        text = text.replace(wordTemplate, word)
    }

    console.log(text);
    
}
