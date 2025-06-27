function cookNums(startNum, word1, word2, word3, word4, word5) {
    let startNumsAsNumber = Number(startNum);
    let wordsList = [word1, word2, word3, word4, word5];

    for (let word of wordsList) {
        if (word === "chop") {
            startNumsAsNumber /= 2;
            console.log(startNumsAsNumber);
        } else if (word === "dice") {
            startNumsAsNumber = Math.sqrt(startNumsAsNumber);
            console.log(startNumsAsNumber);
        } else if (word === "spice") {
            startNumsAsNumber += 1;
            console.log(startNumsAsNumber);
        } else if (word === "bake") {
            startNumsAsNumber *= 3;
            console.log(startNumsAsNumber);
        } else if (word === "fillet") {
            startNumsAsNumber *= 0.80;
            console.log(startNumsAsNumber.toFixed(1));
        }
    }
}