function storeProducts(currentStock, orderedStock) {
    let products = {};
    
    for (let i = 0; i < currentStock.length; i += 2) {
        let product = currentStock[i];
        let quantity = Number(currentStock[i + 1]);

        products[product] = quantity;
    }

    for (let i = 0; i < orderedStock.length; i += 2) {
        let product = orderedStock[i];
        let quantity = Number(orderedStock[i + 1]);

        if (product in products) {
            products[product] += quantity;
        } else {
            products[product] = quantity;
        }
    }

    for (let product in products) {
        console.log(`${product} -> ${products[product]}`);
    }
}
