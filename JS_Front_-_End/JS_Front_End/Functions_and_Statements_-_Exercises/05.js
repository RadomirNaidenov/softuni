function checkIsPalinrom(numbersArray) {

    for (const number of numbersArray) {
        let numAsStr =  String(number);
        let reversednumAsString = numAsStr.split('').reverse().join('');

        if (numAsStr === reversednumAsString) {
            console.log(`true`);
        } else {
            console.log(`false`);   
        }
    }
}