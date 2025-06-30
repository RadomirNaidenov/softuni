function printArray(array, steps) {
    let result = Array();
    

    for (let i = 0; i < array.length; i += steps) {
        result.push(array[i])
    }

    return result  
}
