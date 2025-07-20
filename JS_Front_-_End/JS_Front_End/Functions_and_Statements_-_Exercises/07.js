function makeMatrix(num) {

    for (let i = 1; i <= num; i++) {
        printRow(num)
    }

    function printRow(num) {
        console.log(`${num} `.repeat(num).trim());
    }
}
