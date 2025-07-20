function factorialDivision(num1, num2) {

    let firstFactorial = findFactorial(num1);
    let secondFactorial = findFactorial(num2)

    console.log(`${(firstFactorial / secondFactorial).toFixed(2)}`);

    function findFactorial(num) {
        let sum = 1;

        for (let i = 2; i <= num; i++) {
            sum *= i
        }

        return sum
    }

}