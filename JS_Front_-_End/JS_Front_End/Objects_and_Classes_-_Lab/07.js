function addressBook(array) {
    let personsLocations = {};

    for (const text of array) {
        let [name, address] = text.split(":");

        personsLocations[name] = address;
        
    }

    let sortedPersonLocations = Object.fromEntries(
        Object.entries(personsLocations).sort((a, b) => a[0].localeCompare(b[0])))

    
    for (const [name, location] of Object.entries(sortedPersonLocations)) {
        console.log(`${name} -> ${location}`);
        
    }
    
}
