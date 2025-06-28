function sameNumbers(num) {
    let sum = 0;
    let numAsString = String(num)
    let areSame = true;
    let firstChar = numAsString[0]
       

    for (let i = 0; i < numAsString.length; i++) {
        let currentChar = numAsString[i];

        if (currentChar !== firstChar) {
            areSame = false
        }

        sum += Number(currentChar)

    }

    console.log(areSame);
    console.log(sum);
    
}