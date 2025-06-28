function calcPrice(peopleCount, groupType, day) {
    let singlePrice;
    let totalPrice;

    if (groupType === "Students") {

        if (day === "Friday") {
            singlePrice = 8.45;
        } else if (day === "Saturday") {
            singlePrice = 9.80;
        } else if (day === "Sunday") {
            singlePrice = 10.46;
        }
    }

    if (groupType === "Business") {

        if (day === "Friday") {
            singlePrice = 10.90;
        } else if (day === "Saturday") {
            singlePrice = 15.60;
        } else if (day === "Sunday") {
            singlePrice = 16;
        }
    }

    if (groupType === "Regular") {

        if (day === "Friday") {
            singlePrice = 15;
        } else if (day === "Saturday") {
            singlePrice = 20;
        } else if (day === "Sunday") {
            singlePrice = 22.50;
        }
    }

    totalPrice = singlePrice * peopleCount;

    if (groupType === "Students" && peopleCount >= 30) {
        totalPrice *= 0.85;
    } else if (groupType === "Business" && peopleCount >= 100) {
        totalPrice -= singlePrice * 10
    } else if (groupType === "Regular" && (peopleCount >= 10 && peopleCount <= 20)) {
        totalPrice *= 0.95
    }

    console.log(`Total price: ${totalPrice.toFixed(2)}`);
    
}