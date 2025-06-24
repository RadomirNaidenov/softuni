function calculateCurcleArea(value) {
    let result;

    let inputType = typeof(value)

    if (inputType === "number") {
        result = Math.PI * (value ** 2);
        console.log(result.toFixed(2));
    }

    else {
        console.log(`We can not calculate the circle area, because we receive a ${typeof value}.`);
    }
}

