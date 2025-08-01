function storeHeroInventory(array) {
    let heroes = [];

    for (let str of array) {
        let [heroName, heroLevel, items] = str.split(" / ");
        let splitedItems = items.split(", ");
        
        heroes.push({heroName, heroLevel, splitedItems})
    }

    let sortedArray = heroes.sort((a, b) => a.heroLevel - b.heroLevel)

    sortedArray.forEach(obj => {
        console.log(`Hero: ${obj.heroName}`)
        console.log(`level => ${obj.heroLevel}`)
        console.log(`items => ${obj.splitedItems.join(", ")}`)
    });
}
