function sortNums(array) {
    let sorted = array.sort((a, b) => a - b); 
    let result = [];

    while (sorted.length > 0) {
        let min = sorted.shift();
        result.push(min); 
        let max = sorted.pop();
        result.push(max);
    }

    return result;
}
