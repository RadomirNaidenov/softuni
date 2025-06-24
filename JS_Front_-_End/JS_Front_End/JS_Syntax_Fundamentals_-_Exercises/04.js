function sumNumbers(startNum, endNum) {
    let sequenceOfNums = "";
    let totalSum = 0;

    for (let num = startNum; num <= endNum; num++) {
        sequenceOfNums += num + " ";
        totalSum += num;
    }

    console.log(sequenceOfNums);
    console.log(`Sum: ${totalSum}`);
}
