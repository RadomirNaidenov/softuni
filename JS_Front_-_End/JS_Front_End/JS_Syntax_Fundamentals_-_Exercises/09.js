function fruitInfo(fruit, fruitWeight, pricePerKilo) {
    let weightInKIlo = fruitWeight / 1000
    let totalPrice = weightInKIlo * pricePerKilo

    console.log(`I need $${totalPrice.toFixed(2)} to buy ${weightInKIlo.toFixed(2)} kilograms ${fruit}.`);
    
}