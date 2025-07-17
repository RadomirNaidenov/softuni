function findAsciSymb(char1, char2) {
    let char1ToNum = char1.charCodeAt(0);
    let char2ToNum = char2.charCodeAt(0);

    let fisrtChar = Math.min(char1ToNum, char2ToNum);
    let secondChar = Math.max(char1ToNum, char2ToNum);

    let result = [];

    for (let currentChar = fisrtChar + 1; currentChar < secondChar; currentChar++) {
        result.push(String.fromCharCode(currentChar));
    }

    console.log(result.join(' '));
    
}
