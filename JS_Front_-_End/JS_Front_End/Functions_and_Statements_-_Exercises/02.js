function calculateOperations(num1, num2, num3) {
    let result = 0;

    let sum = (num1, num2) => num1 + num2;
    let subtract = (result, num3) => result - num3;

    result = sum(num1, num2);
    result = subtract(result, num3)

    console.log(result);
    
}
