function findOddAndEvenSumOfNumber(number) {
    let oddSum =  0;
    let evenSum = 0;
    let numberToStr = String(number)
    let numsArray = numberToStr.split('')

    for (let currIndex = 0; currIndex < numsArray.length; currIndex++) {
        let IntNum = Number(numsArray[currIndex]);

        if (IntNum % 2 == 0) {
            evenSum += IntNum;
        } else {
            oddSum += IntNum;
        }
    }

    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
    
}

