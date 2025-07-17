function checkValue(num1, num2, num3) {
    let numsArray = [num1, num2, num3];
    let negativeNumsAray = numsArray.filter(num => num < 0);

    if (negativeNumsAray.length % 2 !== 0) {
        console.log(`Negative`); 
    } else {
        console.log(`Positive`); 
    }
}