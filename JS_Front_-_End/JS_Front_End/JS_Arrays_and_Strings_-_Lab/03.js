function calcSum(array) {
    let oddSum = 0;
    let evenSum = 0;

    for (const num of array) {
        if (num % 2 == 0) {
            evenSum += num;
        } else {
            oddSum += num
        }
    }

    console.log(evenSum - oddSum);
    
}