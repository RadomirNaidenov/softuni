function arrayRotation(array, numOfRotations) {

    for (let num = 0; num < numOfRotations; num++) {
        let element = array.shift();
        array.push(element)
    }

    console.log(array.join(" "));
    
}