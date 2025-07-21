function fromObjectToJson(firstName, lastName, hairColor) {
    let personObject = {
        "name": firstName,
        "lastName": lastName,
        "hairColor": hairColor,
    };

    console.log(JSON.stringify(personObject));
    
}
