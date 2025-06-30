function splitText(text) {
    let words = [];
    let currentWord = text[0];

    for (let i = 1; i < text.length; i++) {
        let currentChar = text[i];

        if (currentChar === currentChar.toUpperCase()) {
            words.push(currentWord);
            currentWord = currentChar;
        } else {
            currentWord += currentChar
        }
    }

    words.push(currentWord)
    console.log(words.join(", "));
    
}