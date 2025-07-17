function calculateValue(numOne, numTwo, operator) {
    let result = 0;

    let add = (a, b) => a + b;
    let divide = (a, b) => a / b;
    let subtract = (a, b) => a - b;
    let multiply = (a, b) => a * b;

    switch(operator) {
        case 'add':
            result = add(numOne, numTwo);
            break;
        case 'divide':
            result = divide(numOne, numTwo);
            break;
        case 'subtract':
            result = subtract(numOne, numTwo);
            break;
        case 'multiply':
            result = multiply(numOne, numTwo);
            break;
    }

    console.log(result);
    
}
