function printObjs(array) {
    let personObj = [];

    for (let str of array) {
        personObj.push({
            name: str,
            number: str.length
        });
    }

    for (let person of personObj) {
        console.log(`Name: ${person.name} -- Personal Number: ${person.number}`);
    }
}
