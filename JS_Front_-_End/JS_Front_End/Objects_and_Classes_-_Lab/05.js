function storesInformation(array) {

    let object = {}

    for (const text of array) {
        let splitedText = text.split(" ");
        let name = splitedText[0];
        let phoneNumber = splitedText[1];
        object[name] = phoneNumber;
    }

    Object.entries(object).forEach(([key, value]) => {
        console.log(`${key} -> ${value}`);
    })
}