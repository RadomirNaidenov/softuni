function sortArray(array) {
    let sortedArray = array.sort((a, b) => a.localeCompare(b));
    let finalResult = []

    for (let index = 0; index < sortedArray.length; index++) {
        finalResult.push(`${index + 1}.${sortedArray[index]}`);
    }

    console.log(finalResult.join(`\n`));
    
}

