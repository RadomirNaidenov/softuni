function determinesPersonType(age) {
    let personType;

    if (0 <= age && age <= 2 ) {
        personType = "baby";
    }

    else if (3 <= age && age <= 13 ) {
        personType = "child";
    }

    else if (14 <= age && age <= 19) {
        personType = "teenager";
    }
    else if (20 <= age && age <= 65) {
        personType = "adult";
    }
    else if (age >= 66) {
        personType = "elder";
    }

    else {
        personType = "out of bounds";
    }

    console.log(personType);
    
}

