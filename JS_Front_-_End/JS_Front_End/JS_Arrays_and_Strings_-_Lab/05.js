function censoreWord(text, word) {
    let censoredWord = "*".repeat(word.length);
    let finalResult = text.replaceAll(word, censoredWord)
    
    console.log(finalResult);
}

