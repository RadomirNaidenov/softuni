function fromJsonToObject(jsonObjet) {
    let personInfoObject = JSON.parse(jsonObjet);

    Object.entries(personInfoObject).forEach(([key, value]) => {
        console.log(`${key}: ${value}`);
        
    })
    
}
