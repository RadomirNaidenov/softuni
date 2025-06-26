function sumOfDigits(num) {
    let totalSum = 0;
    let numAsString = String(num)

    for (let i = 0; i < numAsString.length; i++) {
        let currentNum = Number(numAsString[i]);
        totalSum += currentNum
    }

    console.log(totalSum);
    
}
