function printTownsInfo(array) {
    let arrayOfObj = [];

    for (let str of array) {
        let [town, latitude, longitude] = str.split(" | ");

        latitude = Number(latitude).toFixed(2);
        longitude = Number(longitude).toFixed(2);

        arrayOfObj.push({
            town: town,
            latitude: latitude,
            longitude: longitude
        })
    }

    arrayOfObj.forEach(obg => console.log(obg));
}

['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.363625']
