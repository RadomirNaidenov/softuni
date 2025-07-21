function cityInfo(cityObject) {
    Object.entries(cityObject).forEach(([key, value]) => {
        console.log(`${key} -> ${value}`);    
    })
}
