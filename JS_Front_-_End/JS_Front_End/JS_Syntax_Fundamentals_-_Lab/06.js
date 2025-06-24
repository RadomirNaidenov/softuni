function largestNum(num1, num2, num3) {
    let largest = num1

    if (num2 > num1) {
        largest = num2
    }

    if (num3 > num2) {
        largest = num3
    }

    console.log(`The largest number is ${largest}.`)
}
