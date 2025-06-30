function finsWord(wordToSearch, text) {
    let textArray = text.split(" ");
    let isFound = false;

    for (let word of textArray) {
        if (word.toLowerCase() === wordToSearch.toLowerCase()) {
            isFound = true;
            break;
        } 
    }

    if (isFound) {
        console.log(wordToSearch);
        
    } else {
        console.log(`${wordToSearch} not found!`);
        
    }
}

finsWord('python',
'JavaScript is the best programming language'

)